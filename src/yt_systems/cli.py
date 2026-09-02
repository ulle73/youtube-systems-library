from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

from .index import build_index, search_index
from .ingest import DependencyMissing, ingest_youtube
from .scaffold import scaffold_system
from .timeline import build_timeline
from .transcript import parse_vtt
from .validate import validate_system


def _timeline_from_evidence(evidence_dir: Path) -> list[dict]:
    vtts = sorted(evidence_dir.glob('*.vtt'))
    if not vtts:
        vtts = sorted(evidence_dir.rglob('*.vtt'))
    cues = parse_vtt(vtts[0]) if vtts else []
    frames_json = evidence_dir / 'frames.json'
    frames = json.loads(frames_json.read_text(encoding='utf-8')) if frames_json.exists() else []
    timeline = build_timeline(cues, frames)
    (evidence_dir / 'timeline.json').write_text(json.dumps(timeline, indent=2, ensure_ascii=False), encoding='utf-8')
    lines = ['# Multimodal timeline', '']
    for item in timeline:
        if item['type'] == 'transcript':
            lines.append(f"- `{item['time']:.3f}s` TRANSCRIPT — {item['text']}")
        else:
            lines.append(f"- `{item['time']:.3f}s` FRAME — `{item['path']}`")
    (evidence_dir / 'timeline.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    return timeline


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog='yt-systems', description='Reconstruct source-backed systems from tutorial evidence.')
    sub = parser.add_subparsers(dest='command', required=True)

    p = sub.add_parser('ingest', help='Capture YouTube metadata, captions and media evidence.')
    p.add_argument('url')
    p.add_argument('--out', required=True, type=Path)

    p = sub.add_parser('timeline', help='Build timeline.json and timeline.md from evidence.')
    p.add_argument('evidence_dir', type=Path)

    p = sub.add_parser('scaffold', help='Create a standard system package from evidence.')
    p.add_argument('evidence_dir', type=Path)
    p.add_argument('--out', required=True, type=Path)
    p.add_argument('--slug', required=True)
    p.add_argument('--category', default='unclassified')

    p = sub.add_parser('validate', help='Validate a reconstructed system package.')
    p.add_argument('system_dir', type=Path)

    p = sub.add_parser('index', help='Build a derived Systems Library search index.')
    p.add_argument('systems_root', type=Path)
    p.add_argument('--out', required=True, type=Path)

    p = sub.add_parser('search', help='Search an index by name/category/tool/input/output.')
    p.add_argument('index_path', type=Path)
    p.add_argument('query')
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.command == 'ingest':
            evidence_dir = ingest_youtube(args.url, args.out)
            print(evidence_dir)
            return 0
        if args.command == 'timeline':
            timeline = _timeline_from_evidence(args.evidence_dir)
            print(f'Wrote {len(timeline)} timeline items')
            return 0
        if args.command == 'scaffold':
            path = scaffold_system(args.evidence_dir, args.out, args.slug, args.category)
            print(path)
            return 0
        if args.command == 'validate':
            errors = validate_system(args.system_dir)
            if errors:
                for error in errors:
                    print(error, file=sys.stderr)
                return 1
            print('valid')
            return 0
        if args.command == 'index':
            records = build_index(args.systems_root, args.out)
            print(f'Indexed {len(records)} systems')
            return 0
        if args.command == 'search':
            print(json.dumps(search_index(args.index_path, args.query), indent=2, ensure_ascii=False))
            return 0
    except DependencyMissing as exc:
        print(str(exc), file=sys.stderr)
        return 2
    return 1


if __name__ == '__main__':
    raise SystemExit(main())
