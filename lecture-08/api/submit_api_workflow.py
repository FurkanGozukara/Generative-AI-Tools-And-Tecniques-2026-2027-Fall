"""Adapt one real API export; dry-run, or submit once and poll local ComfyUI."""
import argparse
import json
import time
import uuid
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from inspect_api_workflow import load_workflow


def request(server, route, payload=None, timeout=15, binary=False):
    data = None if payload is None else json.dumps(payload).encode('utf-8')
    req = Request(server.rstrip('/') + route, data=data,
                  headers={'Content-Type': 'application/json'} if data is not None else {})
    try:
        with urlopen(req, timeout=timeout) as response:
            raw = response.read()
    except HTTPError as exc:
        detail = exc.read().decode('utf-8', errors='replace')
        raise RuntimeError(f'HTTP {exc.code}: {detail}') from exc
    return raw if binary else json.loads(raw)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('workflow', type=Path)
    parser.add_argument('--prompt-node', required=True, help='Actual ID from your API export')
    parser.add_argument('--input-name', default='text')
    parser.add_argument('--text', required=True)
    parser.add_argument('--server', default='http://127.0.0.1:8188')
    parser.add_argument('--output', type=Path, default=Path('course_api_outputs'))
    parser.add_argument('--timeout', type=float, default=600, help='Maximum polling time in seconds')
    parser.add_argument('--dry-run', action='store_true', help='Print request; no network calls or output files')
    args = parser.parse_args()
    prompt_id = None
    try:
        if args.timeout <= 0:
            raise ValueError('--timeout must be positive.')
        graph = load_workflow(args.workflow)
        if args.prompt_node not in graph:
            raise ValueError(f'No node {args.prompt_node!r}; run inspect_api_workflow.py on this export.')
        inputs = graph[args.prompt_node]['inputs']
        if args.input_name not in inputs or not isinstance(inputs[args.input_name], str):
            raise ValueError('Choose an existing literal string input, not a link or a numeric widget.')
        inputs[args.input_name] = args.text
        client_id = str(uuid.uuid4())
        payload = {'prompt': graph, 'client_id': client_id}
        if args.dry_run:
            print(json.dumps(payload, ensure_ascii=False, indent=2))
            return

        # A separate folder preserves each request, even if submission or polling fails.
        job_dir = args.output / client_id
        job_dir.mkdir(parents=True, exist_ok=False)
        (job_dir / 'request.json').write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding='utf-8')
        submitted = request(args.server, '/prompt', payload)
        (job_dir / 'submission.json').write_text(json.dumps(submitted, indent=2), encoding='utf-8')
        if submitted.get('error') or not submitted.get('prompt_id'):
            raise RuntimeError(f'Server rejected the workflow: {submitted}')
        prompt_id = submitted['prompt_id']
        print(f'Submitted {prompt_id}; records: {job_dir}', flush=True)
        if submitted.get('node_errors'):
            print(f"Node validation details: {submitted['node_errors']}", flush=True)

        deadline = time.monotonic() + args.timeout
        while True:
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise TimeoutError('Polling timed out; the server job may still be running. Inspect its ID before submitting again.')
            history = request(args.server, '/history/' + str(prompt_id), timeout=min(15, remaining))
            entry = history.get(str(prompt_id))
            if entry:
                status = entry.get('status', {})
                messages = status.get('messages', [])
                failed = status.get('status_str') == 'error' or any(
                    isinstance(m, list) and m and m[0] in ('execution_error', 'execution_interrupted') for m in messages)
                if failed or status.get('completed'):
                    (job_dir / 'history.json').write_text(json.dumps(entry, indent=2), encoding='utf-8')
                    if failed:
                        raise RuntimeError(f'Execution failed: {status}')
                    break
            time.sleep(min(1, max(0, deadline - time.monotonic())))

        # Download file descriptors returned by output nodes. Custom non-file outputs stay in history.json.
        saved = []
        for node_output in entry.get('outputs', {}).values():
            if not isinstance(node_output, dict):
                continue
            for values in node_output.values():
                if not isinstance(values, list):
                    continue
                for item in values:
                    if not isinstance(item, dict) or not isinstance(item.get('filename'), str):
                        continue
                    query = {key: item[key] for key in ('filename', 'subfolder', 'type') if key in item}
                    name = Path(item['filename'].replace('\\', '/')).name
                    if name in ('', '.', '..'):
                        raise ValueError('Invalid output filename from server.')
                    target = job_dir / f'{len(saved)+1:03d}_{name}'
                    target.write_bytes(request(args.server, '/view?' + urlencode(query), binary=True))
                    saved.append(target.name)
        (job_dir / 'downloaded_files.json').write_text(json.dumps(saved, indent=2), encoding='utf-8')
        print(f'Completed {prompt_id}; downloaded {len(saved)} files. Other outputs are in history.json.')
    except (OSError, ValueError, RuntimeError, URLError) as exc:
        suffix = f' Prompt ID: {prompt_id}. Do not resubmit blindly.' if prompt_id else ''
        parser.exit(2, f'Error: {exc}.{suffix}\n')


if __name__ == '__main__':
    main()
