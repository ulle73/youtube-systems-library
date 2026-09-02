from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re


@dataclass(frozen=True)
class Cue:
    start: float
    end: float
    text: str


def _parse_timestamp(value: str) -> float:
    parts = value.strip().split(':')
    if len(parts) == 3:
        h, m, s = parts
    elif len(parts) == 2:
        h, m, s = '0', parts[0], parts[1]
    else:
        raise ValueError(f'Invalid timestamp: {value}')
    return int(h) * 3600 + int(m) * 60 + float(s.replace(',', '.'))


def parse_vtt(path: Path) -> list[Cue]:
    lines = path.read_text(encoding='utf-8-sig').splitlines()
    cues: list[Cue] = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if '-->' not in line:
            i += 1
            continue
        start_s, end_s = [p.strip().split()[0] for p in line.split('-->', 1)]
        i += 1
        text_lines: list[str] = []
        while i < len(lines) and lines[i].strip():
            txt = re.sub(r'<[^>]+>', '', lines[i].strip())
            if txt:
                text_lines.append(txt)
            i += 1
        text = ' '.join(text_lines).strip()
        if text:
            cues.append(Cue(_parse_timestamp(start_s), _parse_timestamp(end_s), text))
        i += 1
    return cues
