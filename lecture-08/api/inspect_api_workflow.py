"""Inspect an actual ComfyUI API export without connecting to a server."""
import argparse
import json
from pathlib import Path


def load_workflow(path):
    graph = json.loads(Path(path).read_text(encoding='utf-8-sig'))
    if not isinstance(graph, dict) or not graph:
        raise ValueError('Expected a non-empty API-format node dictionary.')
    for node_id, node in graph.items():
        if not isinstance(node, dict) or not isinstance(node.get('class_type'), str) or not isinstance(node.get('inputs'), dict):
            raise ValueError('Expected Export (API), not the editor layout JSON. Each node needs class_type and inputs.')
        for name, value in node['inputs'].items():
            if isinstance(value, list) and len(value) == 2 and isinstance(value[0], str) and isinstance(value[1], int):
                if value[0] not in graph or value[1] < 0:
                    raise ValueError(f'{node_id}.{name}: invalid source link {value!r}')
    return graph


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('workflow', type=Path)
    args = parser.parse_args()
    try:
        graph = load_workflow(args.workflow)
        for node_id, node in graph.items():
            print(f"{node_id}: {node['class_type']}")
            for name, value in node['inputs'].items():
                if name in ('text', 'prompt', 'seed', 'noise_seed') or isinstance(value, list):
                    print(f'  {name} = {str(value)[:160]}')
        print('Structure inspected only. Node/model compatibility must be checked on the intended server.')
    except (OSError, ValueError) as exc:
        parser.exit(2, f'Error: {exc}\n')


if __name__ == '__main__':
    main()
