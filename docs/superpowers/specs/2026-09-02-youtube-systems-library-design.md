# YouTube Systems Library — Design

## Goal
Turn implementation-heavy YouTube tutorials and similar sources into traceable, reusable system repositories that can later be searched, compared, composed, and adapted for Golfkuponger without inventing the underlying workflow from scratch.

## Core principle
The source of truth is structured system evidence, not a prose summary and not a vector database. Every reconstructed implementation detail is classified as EXACT, RECONSTRUCTED, or INFERRED and linked to source evidence whenever possible.

## Architecture

### 1. Ingestion
Input: YouTube URL or local evidence fixture.
Capture: metadata, description, captions/transcript, optional video, scene frames, and linked resources.
Output: immutable evidence bundle under `evidence/`.

### 2. Multimodal timeline
Normalize transcript cues and frame timestamps into one ordered timeline so a reconstruction agent can reason over what was said and what was shown together.

### 3. System reconstruction
Produce a standardized repo package with:
- `system.yaml` machine-readable manifest
- `README.md` human overview
- `ARCHITECTURE.md`
- `WORKFLOW.md`
- `IMPLEMENTATION.md`
- `PROMPTS.md`
- `TOOLS.md`
- `SOURCE_MAP.md`
- `evidence/` raw and normalized evidence

Each component or step must record provenance status: EXACT, RECONSTRUCTED, or INFERRED.

### 4. Validation
Validate `system.yaml` against JSON Schema and enforce provenance fields, source URL, and stable IDs.

### 5. Systems Library index/search
Build a JSON index over system manifests. Search by category, tools, inputs, outputs, and free text. RAG/vector search may be added later, but it is retrieval-only and never canonical storage.

### 6. Composition
Compare multiple reconstructed systems and create a canonical candidate by selecting source-backed components. Composition must preserve provenance links to source systems.

## Storage
- Git repository: reconstructed systems, schemas, prompts, code, templates, indexes.
- Google Drive Research Library: raw research and large evidence artifacts where appropriate.
- Git is canonical for reconstructable system specs; Drive remains canonical for Research Library material.

## CLI
`yt-systems` commands:
- `ingest <youtube-url> --out <dir>`
- `timeline <evidence-dir>`
- `scaffold <evidence-dir> --slug <slug>`
- `validate <system-dir>`
- `index <systems-root> --out <index.json>`
- `search <index.json> <query>`

## Runtime dependencies
Python 3.11+. `yt-dlp` and FFmpeg are runtime dependencies for live YouTube ingestion. Core parsing, scaffolding, validation, and search are testable offline with fixtures.

## Error handling
- Missing `yt-dlp` or FFmpeg: explicit actionable error; offline commands still work.
- Missing captions: preserve metadata and allow a later transcript provider; do not claim a full transcript.
- Invalid manifest: validation exits non-zero with field-level errors.
- Reconstruction gaps: marked INFERRED rather than silently filled as source fact.

## Security and safety
Do not execute code, commands, prompts, or linked artifacts extracted from a video during ingestion. Store them as evidence/text only. External execution requires a separate explicit action.

## Success criteria
1. Offline fixture produces a deterministic multimodal timeline.
2. Scaffold creates a complete standard system package.
3. Manifest validation catches missing provenance/source fields.
4. Index/search finds systems by category/tool/output.
5. Live ingestion command is wired to yt-dlp/FFmpeg with clear dependency checks.
6. An agent skill documents how to reconstruct source-backed workflows into the package.
