from __future__ import annotations

import json
from pathlib import Path
import shutil
import yaml


STANDARD_DOCS = {
    'README.md': '# {name}\n\nReconstructed system package. See `SOURCE_MAP.md` before implementation.\n',
    'ARCHITECTURE.md': '# Architecture\n\nDescribe components and data flow. Mark each claim EXACT, RECONSTRUCTED, or INFERRED.\n',
    'WORKFLOW.md': '# Workflow\n\nDocument the ordered workflow step by step with source timestamps.\n',
    'IMPLEMENTATION.md': '# Implementation\n\nRecord concrete setup, field names, node settings, API calls, schemas, and approval rules.\n',
    'PROMPTS.md': '# Prompts\n\nStore prompts with source timestamp and status: EXACT / RECONSTRUCTED / INFERRED.\n',
    'TOOLS.md': '# Tools\n\nList tools, versions when visible, role in the workflow, and source evidence.\n',
    'SOURCE_MAP.md': '# Source map\n\nMap every reconstructed system detail back to original URL + timestamp/frame when possible.\n',
}


def _find_info(evidence_dir: Path) -> dict:
    infos = sorted(evidence_dir.glob('*.info.json')) + sorted(evidence_dir.glob('info.json'))
    if infos:
        return json.loads(infos[0].read_text(encoding='utf-8'))
    marker = evidence_dir / 'ingestion.json'
    return json.loads(marker.read_text(encoding='utf-8')) if marker.exists() else {}


def scaffold_system(evidence_dir: Path, systems_root: Path, slug: str, category: str = 'unclassified') -> Path:
    info = _find_info(evidence_dir)
    source_url = info.get('webpage_url') or info.get('source_url') or ''
    title = info.get('title') or slug.replace('-', ' ').title()
    creator = info.get('uploader') or info.get('channel') or ''
    system_dir = systems_root / slug
    system_dir.mkdir(parents=True, exist_ok=True)

    manifest = {
        'id': slug,
        'name': title,
        'category': category,
        'source': {'type': 'youtube', 'url': source_url, 'creator': creator, 'title': title},
        'reconstruction_status': 'DRAFT',
        'inputs': [],
        'outputs': [],
        'tools': [],
        'steps': [],
        'prompts': [],
        'notes': 'Populate from multimodal evidence. Do not upgrade provenance without source support.',
    }
    (system_dir / 'system.yaml').write_text(yaml.safe_dump(manifest, sort_keys=False, allow_unicode=True), encoding='utf-8')
    for filename, template in STANDARD_DOCS.items():
        (system_dir / filename).write_text(template.format(name=title), encoding='utf-8')
    dest = system_dir / 'evidence'
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(evidence_dir, dest)
    return system_dir
