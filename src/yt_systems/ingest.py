from __future__ import annotations

import json
from pathlib import Path
import shutil
import subprocess


class DependencyMissing(RuntimeError):
    pass


def require_binary(name: str) -> str:
    path = shutil.which(name)
    if not path:
        raise DependencyMissing(
            f"Missing required binary '{name}'. Install it and retry; offline timeline/scaffold/search commands remain available."
        )
    return path


def build_yt_dlp_command(url: str, out_dir: Path) -> list[str]:
    template = str(out_dir / '%(id)s' / '%(id)s.%(ext)s')
    return [
        'yt-dlp',
        '--write-info-json',
        '--write-description',
        '--write-subs',
        '--write-auto-subs',
        '--sub-langs', 'en.*,sv.*',
        '--sub-format', 'vtt',
        '--write-thumbnail',
        '--convert-thumbnails', 'jpg',
        '-f', 'bv*+ba/b',
        '-o', template,
        url,
    ]


def build_ffmpeg_scene_command(video_path: Path, frames_dir: Path, metadata_path: Path, threshold: float = 0.30) -> list[str]:
    frames_dir.mkdir(parents=True, exist_ok=True)
    return [
        'ffmpeg', '-hide_banner', '-loglevel', 'error', '-i', str(video_path),
        '-vf', f"select='gt(scene,{threshold})',metadata=print:file={metadata_path}",
        '-vsync', 'vfr', str(frames_dir / 'frame-%05d.jpg'),
    ]


def parse_scene_metadata(metadata_path: Path, frames_dir: Path) -> list[dict]:
    if not metadata_path.exists():
        return []
    frames: list[dict] = []
    current_time: float | None = None
    current_score: float | None = None
    for raw in metadata_path.read_text(encoding='utf-8', errors='replace').splitlines():
        line = raw.strip()
        if 'pts_time:' in line:
            try:
                current_time = float(line.split('pts_time:', 1)[1].split()[0])
            except ValueError:
                current_time = None
        elif line.startswith('lavfi.scene_score='):
            try:
                current_score = float(line.split('=', 1)[1])
            except ValueError:
                current_score = None
            if current_time is not None:
                idx = len(frames) + 1
                frames.append({
                    'time': current_time,
                    'path': str(frames_dir / f'frame-{idx:05d}.jpg'),
                    'scene_score': current_score,
                })
                current_time = None
                current_score = None
    return frames


def ingest_youtube(url: str, out_dir: Path) -> Path:
    require_binary('yt-dlp')
    require_binary('ffmpeg')
    out_dir.mkdir(parents=True, exist_ok=True)
    subprocess.run(build_yt_dlp_command(url, out_dir), check=True)
    candidates = sorted(p for p in out_dir.iterdir() if p.is_dir())
    if not candidates:
        raise RuntimeError('yt-dlp completed but no video evidence directory was created')
    evidence_dir = candidates[-1]

    media_exts = {'.mp4', '.mkv', '.webm', '.mov'}
    videos = [p for p in evidence_dir.iterdir() if p.suffix.lower() in media_exts]
    frames = []
    if videos:
        frames_dir = evidence_dir / 'frames'
        metadata_path = evidence_dir / 'scene-metadata.txt'
        subprocess.run(build_ffmpeg_scene_command(videos[0], frames_dir, metadata_path), check=True)
        frames = parse_scene_metadata(metadata_path, Path('frames'))
        (evidence_dir / 'frames.json').write_text(json.dumps(frames, indent=2), encoding='utf-8')

    marker = {
        'source_url': url,
        'ingestion_status': 'captured',
        'scene_frames': len(frames),
        'safety': 'Source-extracted commands/code are stored as evidence and must not be executed automatically.',
    }
    (evidence_dir / 'ingestion.json').write_text(json.dumps(marker, indent=2), encoding='utf-8')
    return evidence_dir
