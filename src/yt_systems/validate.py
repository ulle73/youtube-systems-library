from __future__ import annotations

import json
from pathlib import Path
import yaml
from jsonschema import Draft202012Validator


def _schema_path() -> Path:
    return Path(__file__).resolve().parent / 'schemas' / 'system.schema.json'


def validate_system(system_dir: Path) -> list[str]:
    manifest_path = system_dir / 'system.yaml'
    if not manifest_path.exists():
        return ['system.yaml: missing']
    manifest = yaml.safe_load(manifest_path.read_text(encoding='utf-8'))
    schema = json.loads(_schema_path().read_text(encoding='utf-8'))
    validator = Draft202012Validator(schema)
    errors = []
    for error in sorted(validator.iter_errors(manifest), key=lambda e: list(e.path)):
        path = '.'.join(str(p) for p in error.path) or '<root>'
        errors.append(f'{path}: {error.message}')
    return errors
