from __future__ import annotations

import json
from pathlib import Path
import re
import yaml


def build_index(systems_root: Path, out_path: Path) -> list[dict]:
    records: list[dict] = []
    for manifest_path in sorted(systems_root.glob('*/system.yaml')):
        data = yaml.safe_load(manifest_path.read_text(encoding='utf-8')) or {}
        record = {
            'id': data.get('id',''),
            'name': data.get('name',''),
            'category': data.get('category',''),
            'tools': data.get('tools',[]) or [],
            'inputs': data.get('inputs',[]) or [],
            'outputs': data.get('outputs',[]) or [],
            'status': data.get('reconstruction_status',''),
            'source_url': (data.get('source') or {}).get('url',''),
            'path': str(manifest_path.parent),
        }
        record['search_text'] = ' '.join([
            record['id'], record['name'], record['category'],
            *map(str, record['tools']), *map(str, record['inputs']), *map(str, record['outputs'])
        ]).lower()
        records.append(record)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(records, indent=2, ensure_ascii=False), encoding='utf-8')
    return records


def search_index(index_path: Path, query: str) -> list[dict]:
    records = json.loads(index_path.read_text(encoding='utf-8'))
    terms = [t.lower() for t in re.findall(r'[\w+.-]+', query) if t.strip()]
    scored = []
    for record in records:
        text = record.get('search_text','')
        score = sum(text.count(term) for term in terms)
        if score:
            result = dict(record)
            result['score'] = score
            scored.append(result)
    return sorted(scored, key=lambda r: (-r['score'], r['name'].lower()))
