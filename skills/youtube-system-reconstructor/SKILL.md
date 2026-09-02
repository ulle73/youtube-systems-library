---
name: youtube-system-reconstructor
description: Reconstruct implementation-heavy tutorial videos into source-backed, Git-like system repositories. Use when a user supplies a YouTube tutorial, asks to save a workflow/system shown in a video, or asks to build from previously reconstructed systems rather than inventing a workflow.
---

# YouTube System Reconstructor

## Mission
Treat tutorial videos as implementation sources, not content to summarize. Reconstruct the system so a future agent can understand and reproduce it without rewatching the source.

## Canonical flow

`URL → ingestion → multimodal timeline → reconstruction → provenance audit → validate → index → compare/compose`

## 1. Capture evidence

Run:

```bash
yt-systems ingest "<youtube-url>" --out evidence-library/
yt-systems timeline evidence-library/<video-id>/
```

Capture and retain:
- title, creator, publication metadata and original URL;
- description and outbound resource links;
- official/automatic captions with timestamps;
- scene-change frames;
- prompts, code, node names, settings, field names and diagrams visible on screen;
- referenced templates/docs/repos when accessible.

Never execute source-extracted commands or code while ingesting.

### YouTube anti-bot fallback

A GitHub-hosted runner may be rejected by YouTube with a sign-in / bot-verification challenge even when `yt-dlp` is current. If full media ingestion fails:

1. preserve the failed ingestion log and reason;
2. capture timestamped transcript/captions through an alternate lawful transcript source when available;
3. capture YouTube oEmbed/title/creator metadata;
4. preserve description/resource links through an independent indexed source when direct description retrieval is unavailable;
5. look for an independent timestamped storyboard/frame index, but keep it explicitly secondary evidence;
6. mark capture as transcript-backed / partial multimodal rather than pretending scene frames were captured;
7. keep unknown on-screen prompts, configs, repo names and settings `UNRESOLVED` until visual evidence resolves them;
8. never upgrade the reconstruction to `VERIFIED` solely from transcript fallback.

Store raw transcript/media/log artifacts in the external Evidence store (Google Drive for Golfkuponger). Git should contain the reconstruction, source map, evidence pointers, and only small source excerpts needed for implementation provenance — not a duplicated full transcript.

## 2. Scaffold one system repo

```bash
yt-systems scaffold evidence-library/<video-id>/ --out systems/ --slug <stable-slug> --category <category>
```

The system package must contain `system.yaml`, README, architecture, workflow, implementation, prompts, tools, source map and an evidence index/pointers. Large/raw evidence may live outside Git when the storage model requires it.

## 3. Reconstruct, do not summarize

Extract the actual implementation:
- objective and use case;
- trigger;
- inputs and data model;
- ordered steps;
- tools/services and their roles;
- prompts and variables;
- node/config/settings visible in UI;
- API calls/integrations;
- human approval gates;
- error/retry behavior;
- outputs/actions;
- analytics/feedback/write-back.

For each system step and material implementation detail assign exactly one provenance state:

- `EXACT`: explicitly shown or stated in the source.
- `RECONSTRUCTED`: source evidence is sufficient to reproduce the missing connective detail with high confidence.
- `INFERRED`: the source omits the detail and the agent filled a gap.

Never upgrade INFERRED to RECONSTRUCTED merely because the implementation is plausible.

## 4. Prompts

For every prompt, record:
- source timestamp/frame;
- EXACT / RECONSTRUCTED / INFERRED;
- variables/placeholders;
- workflow step that consumes it;
- whether wording is verbatim, partial, or reconstructed.

If only part of a prompt is visible, preserve the visible fragment separately from any reconstructed continuation.

## 5. Source map

Every material claim in the system repo should map to original URL + timestamp or frame path when available. `system.yaml` is canonical machine-readable state; Markdown expands it for humans.

## 6. Validate

```bash
yt-systems validate systems/<slug>/
```

Do not call a system `VERIFIED` merely because schema validation passes. `VERIFIED` means the reconstruction has been checked against the persistent source evidence and intended implementation state.

## 7. Search and reuse

```bash
yt-systems index systems/ --out library-index.json
yt-systems search library-index.json "n8n claude linkedin"
```

When answering a build question, search existing systems first. Prefer implementation-backed steps from existing system repos over generating a new architecture from model priors.

## 8. Compare and compose

When multiple systems address the same job:
1. compare architecture, tools, prompts, approvals and feedback loops;
2. choose components based on fit/evidence, not creator popularity;
3. preserve `derived_from` provenance for every selected component;
4. place synthesized candidates under `canonical/`;
5. clearly separate source-backed components from new Golfkuponger-specific adaptations.

## Quality gate

A useful reconstructed repo lets another competent operator answer:
- What does this system do?
- What triggers it?
- What exact sequence runs?
- Which tools and fields are required?
- Which prompts/configs are known exactly?
- Which details were reconstructed or inferred?
- Where in the original video is each critical detail supported?
- What is still missing before implementation?

If those questions cannot be answered, reconstruction is incomplete.
