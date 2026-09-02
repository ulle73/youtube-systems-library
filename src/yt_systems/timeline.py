from __future__ import annotations

from .transcript import Cue


def build_timeline(cues: list[Cue], frames: list[dict]) -> list[dict]:
    items: list[dict] = []
    for cue in cues:
        items.append({
            'type': 'transcript',
            'time': cue.start,
            'end': cue.end,
            'text': cue.text,
        })
    for frame in frames:
        items.append({'type': 'frame', 'time': float(frame['time']), 'path': frame['path']})
    return sorted(items, key=lambda x: (x['time'], 0 if x['type'] == 'transcript' else 1))
