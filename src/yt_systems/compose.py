from __future__ import annotations

from copy import deepcopy


def compare_systems(systems: list[dict]) -> dict:
    tool_sets = [set(s.get('tools', [])) for s in systems]
    shared = sorted(set.intersection(*tool_sets)) if tool_sets else []
    unique = {}
    for system, tools in zip(systems, tool_sets):
        others = set().union(*(ts for ts in tool_sets if ts is not tools)) if len(tool_sets) > 1 else set()
        unique[system['id']] = sorted(tools - others)
    return {
        'shared_tools': shared,
        'unique_tools': unique,
        'outputs': {s['id']: sorted(s.get('outputs', [])) for s in systems},
    }


def compose_candidate(candidate_id: str, name: str, systems: list[dict], selections: list[tuple[str, str]]) -> dict:
    by_id = {s['id']: s for s in systems}
    steps = []
    for system_id, step_id in selections:
        system = by_id[system_id]
        step = next(s for s in system.get('steps', []) if s['id'] == step_id)
        copied = deepcopy(step)
        copied['derived_from'] = {
            'system_id': system_id,
            'system_name': system.get('name', system_id),
            'source_url': (system.get('source') or {}).get('url', ''),
            'step_id': step_id,
        }
        steps.append(copied)
    return {
        'id': candidate_id,
        'name': name,
        'category': 'canonical-candidate',
        'reconstruction_status': 'DRAFT',
        'steps': steps,
        'source_systems': sorted({sid for sid, _ in selections}),
    }
