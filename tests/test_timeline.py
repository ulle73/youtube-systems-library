from pathlib import Path
from yt_systems.transcript import parse_vtt
from yt_systems.timeline import build_timeline


def test_parse_vtt_returns_timestamped_cues():
    cues = parse_vtt(Path('tests/fixtures/sample.vtt'))
    assert cues[0].start == 1.0
    assert cues[0].end == 4.0
    assert cues[0].text == 'Open n8n and create a webhook node.'


def test_timeline_merges_frames_in_time_order():
    cues = parse_vtt(Path('tests/fixtures/sample.vtt'))
    frames = [
        {'time': 3.2, 'path': 'frames/frame-0001.jpg'},
        {'time': 7.0, 'path': 'frames/frame-0002.jpg'},
    ]
    timeline = build_timeline(cues, frames)
    assert [item['type'] for item in timeline] == ['transcript', 'frame', 'transcript', 'frame']
    assert timeline[1]['path'].endswith('frame-0001.jpg')
