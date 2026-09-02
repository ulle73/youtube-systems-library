from pathlib import Path
import pytest
from yt_systems.ingest import DependencyMissing, build_yt_dlp_command, require_binary


def test_build_yt_dlp_command_captures_metadata_description_subtitles_and_video(tmp_path: Path):
    cmd = build_yt_dlp_command('https://youtube.com/watch?v=abc', tmp_path)
    joined = ' '.join(cmd)
    assert '--write-info-json' in cmd
    assert '--write-description' in cmd
    assert '--write-subs' in cmd
    assert '--write-auto-subs' in cmd
    assert 'https://youtube.com/watch?v=abc' == cmd[-1]
    assert str(tmp_path) in joined


def test_require_binary_raises_actionable_error(monkeypatch):
    monkeypatch.setattr('shutil.which', lambda name: None)
    with pytest.raises(DependencyMissing, match='yt-dlp'):
        require_binary('yt-dlp')

from yt_systems.ingest import parse_scene_metadata


def test_parse_scene_metadata_maps_pts_times_to_frame_paths(tmp_path: Path):
    meta = tmp_path/'scene-metadata.txt'
    meta.write_text('frame:0 pts:100 pts_time:3.25\nlavfi.scene_score=0.44\nframe:1 pts:200 pts_time:8.5\nlavfi.scene_score=0.51\n', encoding='utf-8')
    frames = parse_scene_metadata(meta, Path('frames'))
    assert frames == [
        {'time': 3.25, 'path': 'frames/frame-00001.jpg', 'scene_score': 0.44},
        {'time': 8.5, 'path': 'frames/frame-00002.jpg', 'scene_score': 0.51},
    ]
