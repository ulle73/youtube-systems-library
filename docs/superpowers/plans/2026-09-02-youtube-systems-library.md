# YouTube Systems Library Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a tested CLI and repository format that converts YouTube tutorial evidence into traceable system packages and a searchable Systems Library.

**Architecture:** Separate ingestion, timeline normalization, reconstruction scaffolding, validation, and index/search. Live YouTube dependencies are isolated behind subprocess wrappers so the core can be tested offline.

**Tech Stack:** Python 3.11+, pytest, PyYAML, jsonschema, yt-dlp, FFmpeg.

**Spec:** `docs/superpowers/specs/2026-09-02-youtube-systems-library-design.md`

## Global Constraints
- Every reconstructed detail uses EXACT, RECONSTRUCTED, or INFERRED provenance.
- Structured manifests are canonical; retrieval indexes are derived.
- Do not execute source-extracted code during ingestion.
- Core tests must run without network access.

---

### Task 1: Package skeleton and provenance model
**Files:** `pyproject.toml`, `src/yt_systems/models.py`, `tests/test_models.py`
- [ ] Write failing provenance tests.
- [ ] Run tests and verify RED.
- [ ] Implement enums/dataclasses and serialization helpers.
- [ ] Run tests and verify GREEN.

### Task 2: Transcript and multimodal timeline
**Files:** `src/yt_systems/transcript.py`, `src/yt_systems/timeline.py`, `tests/test_timeline.py`, fixtures.
- [ ] Write failing VTT/timeline tests.
- [ ] Verify RED.
- [ ] Implement parser and timeline merger.
- [ ] Verify GREEN.

### Task 3: YouTube ingestion wrappers
**Files:** `src/yt_systems/ingest.py`, `tests/test_ingest.py`
- [ ] Write failing command-construction/dependency tests.
- [ ] Verify RED.
- [ ] Implement safe yt-dlp/FFmpeg wrappers and metadata output.
- [ ] Verify GREEN.

### Task 4: Manifest schema and scaffold
**Files:** `schemas/system.schema.json`, `src/yt_systems/scaffold.py`, templates, `tests/test_scaffold.py`.
- [ ] Write failing scaffold/schema tests.
- [ ] Verify RED.
- [ ] Implement deterministic standard repo generator.
- [ ] Verify GREEN.

### Task 5: Validation
**Files:** `src/yt_systems/validate.py`, `tests/test_validate.py`.
- [ ] Write failing validation tests.
- [ ] Verify RED.
- [ ] Implement JSON Schema validation and provenance checks.
- [ ] Verify GREEN.

### Task 6: Index and search
**Files:** `src/yt_systems/index.py`, `tests/test_index.py`.
- [ ] Write failing index/search tests.
- [ ] Verify RED.
- [ ] Implement deterministic index and ranked text/filter search.
- [ ] Verify GREEN.

### Task 7: CLI and skill
**Files:** `src/yt_systems/cli.py`, `skills/youtube-system-reconstructor/SKILL.md`, `README.md`, `tests/test_cli.py`.
- [ ] Write failing CLI smoke tests.
- [ ] Verify RED.
- [ ] Implement CLI wiring and reconstruction skill instructions.
- [ ] Verify GREEN.

### Task 8: End-to-end verification
- [ ] Run full pytest suite.
- [ ] Build package.
- [ ] Execute fixture timeline/scaffold/validate/index/search flow.
- [ ] Inspect git diff and commit verified implementation.
