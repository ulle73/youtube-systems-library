# YouTube Systems Library

A source-backed **“GitHub for tutorial workflows.”** It turns implementation-heavy YouTube videos into reusable system repositories instead of disposable summaries.

## Why

Tutorial creators often show complete automation systems, prompts, n8n/Make/Zapier flows, database schemas and configs without publishing a cloneable repository. This project captures the video as multimodal evidence and reconstructs the implementation into a standard, searchable repo format.

## Core pipeline

```text
YouTube URL
  → yt-dlp metadata + description + captions + media
  → FFmpeg scene-change frames
  → timestamp-aligned multimodal timeline
  → agent reconstruction
  → EXACT / RECONSTRUCTED / INFERRED provenance
  → system.yaml + implementation docs
  → schema validation
  → Systems Library index/search
  → compare + canonical composition
```

## Install

```bash
python -m pip install -e '.[youtube,dev]'
```

Live ingestion also requires `ffmpeg` on PATH.

## Quick start

```bash
# 1. Capture evidence
yt-systems ingest "https://www.youtube.com/watch?v=..." --out evidence-library/

# 2. Build transcript + frame timeline
yt-systems timeline evidence-library/<video-id>/

# 3. Create a system repo
yt-systems scaffold evidence-library/<video-id>/ \
  --out systems/ \
  --slug multi-channel-content-engine \
  --category content-creation

# 4. Use skills/youtube-system-reconstructor/SKILL.md with Codex/Claude/ChatGPT
#    to populate system.yaml and docs from timeline + frames.

# 5. Enforce schema/evidence requirements
yt-systems validate systems/multi-channel-content-engine/

# 6. Search the library
yt-systems index systems/ --out library-index.json
yt-systems search library-index.json "n8n claude linkedin"
```

## System repo format

```text
systems/<system-id>/
├── system.yaml          # canonical machine-readable system manifest
├── README.md
├── ARCHITECTURE.md
├── WORKFLOW.md
├── IMPLEMENTATION.md
├── PROMPTS.md
├── TOOLS.md
├── SOURCE_MAP.md
└── evidence/
    ├── *.info.json
    ├── *.description
    ├── *.vtt
    ├── frames/
    ├── frames.json
    ├── timeline.json
    └── timeline.md
```

## Provenance contract

Every material step is one of:

- **EXACT** — directly shown/stated.
- **RECONSTRUCTED** — enough source evidence exists to reproduce the connective detail with high confidence.
- **INFERRED** — source omitted it; the agent filled the gap.

This distinction is what keeps a reconstructed tutorial repo from becoming an AI-generated fiction.

## Storage model for Golfkuponger

- **Research Library / Google Drive:** external research, transcripts, evidence and syntheses.
- **Systems Library / Git:** reconstructed implementation repos, prompts, schemas, code/configs and canonical composed systems.
- **Search/RAG:** derived retrieval layer only, never source of truth.

## Tests

```bash
pytest -q
```

The core suite is network-free. Live YouTube ingestion is intentionally isolated behind `yt-dlp` + FFmpeg.
