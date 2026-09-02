from pathlib import Path
import json
import yaml
from yt_systems.scaffold import scaffold_system


def test_scaffold_creates_standard_system_package(tmp_path: Path):
    evidence = tmp_path / 'evidence'
    evidence.mkdir()
    (evidence / 'info.json').write_text(json.dumps({
        'title': 'Build a Content Engine',
        'webpage_url': 'https://youtube.com/watch?v=abc',
        'uploader': 'Example Creator'
    }), encoding='utf-8')
    out = tmp_path / 'systems'
    system_dir = scaffold_system(evidence, out, 'content-engine')
    expected = {
        'system.yaml', 'README.md', 'ARCHITECTURE.md', 'WORKFLOW.md',
        'IMPLEMENTATION.md', 'PROMPTS.md', 'TOOLS.md', 'SOURCE_MAP.md', 'evidence'
    }
    assert expected.issubset({p.name for p in system_dir.iterdir()})
    manifest = yaml.safe_load((system_dir / 'system.yaml').read_text())
    assert manifest['id'] == 'content-engine'
    assert manifest['source']['url'] == 'https://youtube.com/watch?v=abc'
    assert manifest['reconstruction_status'] == 'DRAFT'
    assert manifest['steps'] == []
