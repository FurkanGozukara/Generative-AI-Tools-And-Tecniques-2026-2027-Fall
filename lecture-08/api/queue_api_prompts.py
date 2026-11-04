"""Queue several prompts through one real API export, optionally cancel the last waiting job, and report every outcome.

Extends submit_api_workflow.py (same request helper and the same per-run records). Each prompt gets its own file name prefix,
so the saved images never overwrite each other. Outcomes:
  completed  the history entry finished; its files are downloaded
  failed     the history entry holds an execution error
  cancelled  the job was removed from the queue before it started
  rejected   the server refused the request, so there is no job ID
  unknown    the client stopped waiting; look the ID up in the history before submitting again
"""
import argparse
import copy
import json
import time
import uuid
from pathlib import Path
from urllib.parse import urlencode

from inspect_api_workflow import load_workflow
from submit_api_workflow import request


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('workflow', type=Path)
    parser.add_argument('--prompt-node', required=True, help='Node ID whose text input receives each prompt')
    parser.add_argument('--input-name', default='text')
    parser.add_argument('--save-node', required=True, help='Node ID of the saver whose filename_prefix gets a unique name')
    parser.add_argument('--prompts', type=Path, required=True, help='Text file, one prompt per line')
    parser.add_argument('--prefix', default='Lecture08/queue')
    parser.add_argument('--server', default='http://127.0.0.1:8188')
    parser.add_argument('--output', type=Path, default=Path('course_api_outputs'))
    parser.add_argument('--timeout', type=float, default=600)
    parser.add_argument('--cancel-last', action='store_true', help='Remove the last job from the queue while it is still waiting')
    args = parser.parse_args()

    graph = load_workflow(args.workflow)
    for node, name in ((args.prompt_node, args.input_name), (args.save_node, 'filename_prefix')):
        if node not in graph or not isinstance(graph[node]['inputs'].get(name), str):
            parser.exit(2, f'Error: node {node!r} has no literal {name!r} input; run inspect_api_workflow.py first.\n')
    prompts = [line.strip() for line in args.prompts.read_text(encoding='utf-8').splitlines() if line.strip()]
    if not prompts:
        parser.exit(2, 'Error: the prompts file is empty.\n')

    run_dir = args.output / ('queue_' + time.strftime('%Y%m%d_%H%M%S'))
    run_dir.mkdir(parents=True, exist_ok=False)
    client_id = str(uuid.uuid4())
    jobs = []
    for number, text in enumerate(prompts, 1):
        job = copy.deepcopy(graph)
        job[args.prompt_node]['inputs'][args.input_name] = text
        job[args.save_node]['inputs']['filename_prefix'] = f'{args.prefix}_{number}'
        row = {'job': number, 'prompt': text, 'prefix': f'{args.prefix}_{number}', 'prompt_id': None, 'outcome': None, 'files': []}
        (run_dir / f'job{number}_request.json').write_text(json.dumps({'prompt': job, 'client_id': client_id}, indent=2), encoding='utf-8')
        try:
            answer = request(args.server, '/prompt', {'prompt': job, 'client_id': client_id})
        except RuntimeError as exc:
            answer = {'error': str(exc)}
        if answer.get('prompt_id') and not answer.get('error'):
            row['prompt_id'] = answer['prompt_id']
            print(f'Job {number} submitted: {row["prompt_id"]}', flush=True)
        else:
            row['outcome'] = 'rejected'
            print(f'Job {number} rejected: {answer.get("error")}', flush=True)
        jobs.append(row)

    if args.cancel_last and jobs[-1]['prompt_id']:
        last = jobs[-1]
        queue = request(args.server, '/queue')
        waiting = {item[1] for item in queue.get('queue_pending', [])}
        if last['prompt_id'] in waiting:
            request(args.server, '/queue', {'delete': [last['prompt_id']]}, binary=True)   # the server answers with an empty body
            last['outcome'] = 'cancelled'
            print(f'Job {last["job"]} cancelled while it was still waiting', flush=True)
        else:
            print(f'Job {last["job"]} had already started; it was not cancelled', flush=True)

    deadline = time.monotonic() + args.timeout
    for row in jobs:
        if row['outcome']:
            continue
        while True:
            entry = request(args.server, '/history/' + row['prompt_id']).get(row['prompt_id'])
            status = (entry or {}).get('status', {})
            messages = [m[0] for m in status.get('messages', []) if isinstance(m, list) and m]
            if entry and (status.get('status_str') == 'error' or 'execution_error' in messages):
                row['outcome'] = 'failed'
                break
            if entry and status.get('completed'):
                row['outcome'] = 'completed'
                for output in entry.get('outputs', {}).values():
                    for item in output.get('images', []):
                        query = {key: item[key] for key in ('filename', 'subfolder', 'type') if key in item}
                        target = run_dir / f'job{row["job"]}_{Path(item["filename"]).name}'
                        target.write_bytes(request(args.server, '/view?' + urlencode(query), binary=True))
                        row['files'].append(target.name)
                break
            if time.monotonic() > deadline:
                row['outcome'] = 'unknown'
                break
            time.sleep(1)
        (run_dir / f'job{row["job"]}_history.json').write_text(json.dumps(entry or {}, indent=2), encoding='utf-8')

    (run_dir / 'summary.json').write_text(json.dumps(jobs, indent=2), encoding='utf-8')
    print()
    print('Job  Outcome    Prompt ID                             Files')
    for row in jobs:
        print(f'{row["job"]:<4} {row["outcome"]:<10} {row["prompt_id"] or "-":<37} {", ".join(row["files"]) or "-"}')
    print(f'Records: {run_dir}')


if __name__ == '__main__':
    main()
