from pathlib import Path
import json
from yt_systems.cli import main


def test_cli_timeline_writes_json(tmp_path: Path):
    evidence = tmp_path/'evidence'; evidence.mkdir()
    (evidence/'sample.vtt').write_text('WEBVTT\n\n00:00:01.000 --> 00:00:02.000\nHello system.\n', encoding='utf-8')
    rc = main(['timeline', str(evidence)])
    assert rc == 0
    data = json.loads((evidence/'timeline.json').read_text())
    assert data[0]['text'] == 'Hello system.'


def test_cli_validate_returns_nonzero_for_missing_manifest(tmp_path: Path):
    rc = main(['validate', str(tmp_path)])
    assert rc == 1
