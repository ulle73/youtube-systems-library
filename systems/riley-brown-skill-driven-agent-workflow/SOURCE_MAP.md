# Source Map

Primary video source: https://www.youtube.com/watch?v=N34zz1-RSGw
Primary implementation corroboration: https://github.com/rbrown101010/rileys-skills

Capture status: **transcript-backed + primary public skill-repository corroboration; partial multimodal**. Do not treat video UI-specific details as frame-verified.

## Video evidence

| Source time | Evidence | Provenance | System implication |
|---|---|---|---|
| 03:16–07:29 | Reusable skills around agent work, video/visual work, image retrieval and YouTube research | EXACT_VIDEO | Domain procedures can be encapsulated as reusable skill primitives. |
| 08:25–09:29 | Extract successful hook/outline structure and reuse it; parallel research mentioned | EXACT_VIDEO | Repeated analytical transformations can become reusable decision/workflow skills. |
| 10:15–12:04 | Selective scripting and outcome-oriented framing | EXACT_VIDEO | Preserve human-authored substance; encode repetitive packaging/research assistance rather than replacing every judgment step. |
| 13:28–15:03 | BRENS: Big, Relatable, Easy, New, Safe | EXACT_VIDEO | Example of explicit judgment criteria that can be packaged into a skill. |
| 15:09–17:20 | Main content/curiosity can precede final packaging; AI analyzes finished material | EXACT_VIDEO | Workflow order can follow information availability rather than a rigid template. |
| 17:24–18:42 | Excalidraw, thumbnail and Typefully-related skill examples | EXACT_VIDEO | Skill library can contain specialized primitives with distinct outputs. |
| 19:04–19:16 | Useful repeated AI work is turned into a skill; some skills later stop being used | EXACT_VIDEO | Bottom-up promotion and natural skill lifecycle. |
| 20:17–21:56 | Notion/Docs/calendar/email integrations reduce tab switching | EXACT_VIDEO | Connect reusable workflows to systems of record/action when valuable. |
| 22:10–25:08 | AI used for deeper research, fact checking, visual planning and structuring ideas, not only batching | EXACT_VIDEO | Optimize quality/depth, not automation volume. |
| 25:43–31:01 | Visual reference board, variants and human selection | EXACT_VIDEO | Human taste remains a selection/quality gate. |
| 31:15–31:55 | Skills are mixed and matched into new workflows | EXACT_VIDEO | Composition is a capability multiplier. |
| 32:08–33:07 | Run skill → judge output → describe failure → update → fresh chat/context → retest | EXACT_VIDEO | Core outcome-refinement and fresh-context QA loop. |
| 33:23–33:45 | Higher-risk work deserves explicit inspection/review | EXACT_VIDEO | Risk-dependent audit boundary. |
| 34:53–37:58 | Local vs cloud execution; unattended recurring tasks benefit from cloud runtime | EXACT_VIDEO | Separate workflow logic from deployment environment. |
| 38:00–40:00 | Expertise/content strengthened by doing real work rather than only aggregating | EXACT_VIDEO at principle level | Operational learning should feed durable knowledge. |

## Primary public repository evidence

| Artifact | Evidence | Provenance | System implication |
|---|---|---|---|
| `rileys-skills/README.md` | Personal Codex skills are manually maintained under `~/.codex/skills`; portable instructions/scripts/references/metadata/templates/assets are stored in skill folders | EXACT_PRIMARY_REPO | Riley's reusable capability layer is filesystem-backed and package-oriented, not just conversational memory. |
| `youtube-researcher/SKILL.md` + helper | SerpAPI is used for YouTube search; Supadata for transcripts/channel/video metadata; helper normalizes results and synthesis is done by the agent/chat | EXACT_PRIMARY_REPO | Separate deterministic retrieval/data plumbing from higher-level analysis and judgment. |
| `internet-image-puller/SKILL.md` | SerpAPI performs query-driven image discovery; Firecrawl handles page/site extraction; output includes local assets plus a manifest/dedupe behavior | EXACT_PRIMARY_REPO | Asset retrieval can be a reusable primitive with a durable artifact contract. |
| `youtube-thumbnail/SKILL.md` | Explicitly depends on `youtube-researcher`, `internet-image-puller`, and image generation/editing | EXACT_PRIMARY_REPO | Direct implementation proof of skill composition by dependency reuse. |
| `excalidraw-diagrams/SKILL.md` | Structured diagram plan is translated to Excalidraw JSON, run through CLI, previewed/exported as editable artifact | EXACT_PRIMARY_REPO | Skills can combine judgment rules with deterministic executable artifact generation. |
| `notion-full-control/SKILL.md` | Local wrapper handles search/get/query/create/update/append/raw operations and inspects schema before writes | EXACT_PRIMARY_REPO | Exact system-of-record operations can live behind a controlled tool wrapper. |
| `typefully-control/SKILL.md` | API wrapper covers drafts/publishing/queue/analytics; tests default to draft creation unless live publish is explicitly requested | EXACT_PRIMARY_REPO | Reversible defaults and explicit live-action boundaries can be encoded into action skills. |
| public YouTube helper | Contains hardcoded default API credentials in source | EXACT_PRIMARY_REPO_SECURITY_FINDING | This is a security flaw, not a reusable pattern; credential values are intentionally excluded and must be treated as exposed. |

## Reconstructed connective model
The canonical lifecycle used in this repository — `real work → repetition → skill → outcome test → feedback → fresh-context retest → composition → risk gate → execution environment` — is **RECONSTRUCTED** from the video segments above. Riley does not present it as one named framework in this exact form.

The implementation architecture — `skill/orchestration → script/CLI/other skill → API/tool → artifact/state → human judgment` — is **RECONSTRUCTED** from multiple primary public skill implementations. Individual links in the chain are directly evidenced, but Riley does not state this as one formal architecture.

## Evidence caveat
The preferred Apify transcript actor could not run on 2026-09-11 because the connected account had reached its monthly usage hard limit. Public transcript sources preserve the video timestamp evidence, while Riley's public skill repository provides primary implementation corroboration. Direct full-video frame capture is still incomplete, so UI-specific visual details remain unresolved unless separately verified.
