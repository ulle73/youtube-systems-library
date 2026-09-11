# Tools

This system is tool-agnostic at its core. Tool names below are source examples and primary-repo evidence, not architectural requirements for Golfkuponger.

## Codex / local agent workspace
- **Source state:** EXACT from interview.
- **Role:** interactive agent environment where Riley runs tasks, uses local skills and composes workflows against local files/computer context.
- **Durable lesson:** the agent work surface can stay flexible while repeatable procedures live in reusable skill packages.

## Riley's filesystem skill library
- **Source state:** EXACT_PRIMARY_REPO.
- **Evidence:** public `rileys-skills` README says personal Codex skills are manually maintained under `~/.codex/skills` and portable skill files/scripts/references/templates/assets are stored inside their folders.
- **Role:** versionable reusable capability layer.
- **Durable lesson:** a skill is an operational package, not merely a remembered chat instruction.

## YouTube Researcher
- **Source state:** EXACT from interview + EXACT_PRIMARY_REPO.
- **Role:** niche/video search, channel inspection, transcript retrieval and structured research input.
- **Implementation:** local Python helper; SerpAPI handles YouTube search; Supadata handles transcripts, channel metadata, channel videos and video metadata; chat/agent performs synthesis.
- **Durable lesson:** separate retrieval from higher-level judgment/synthesis.

## Internet Image Puller
- **Source state:** EXACT from interview + EXACT_PRIMARY_REPO.
- **Role:** find/download logos, brand assets, moodboard/reference images and page/site images.
- **Implementation:** SerpAPI for query-driven Google Images discovery; Firecrawl for page/site extraction; downloaded files plus `manifest.json`, sanitization and deduplication.
- **Durable lesson:** asset retrieval is a standalone primitive that other visual workflows can reuse.

## Remotion / Remotion best-practices skill
- **Source state:** EXACT at interview level; exact private/local configuration not fully available.
- **Role:** create motion graphics/B-roll; Riley describes a best-practices layer carrying his creator-brand styling/defaults.
- **Durable lesson:** reusable domain rules and brand/style defaults can sit above a production tool.

## YouTube Thumbnail skill
- **Source state:** EXACT_PRIMARY_REPO.
- **Role:** higher-order composite workflow for thumbnail generation from high-performing references, person images and optional supporting assets.
- **Dependencies:** `youtube-researcher` for YouTube reference discovery; `internet-image-puller` for logos/assets; OpenAI image generation/editing for final 16:9 variants.
- **Durable lesson:** composition can be explicit dependency reuse rather than duplicating primitive logic.

## Excalidraw Diagrams
- **Source state:** EXACT from interview + EXACT_PRIMARY_REPO.
- **Role:** turn text/structured plans into editable diagrams.
- **Implementation:** plan nodes/arrows/labels, translate to Excalidraw JSON elements, run `excalidraw-cli`, optionally create a preview and export a shareable URL.
- **Durable lesson:** a skill can encode both judgment rules and an executable artifact contract.

## Paper / Paper Deck Style
- **Source state:** EXACT as source example + EXACT_PRIMARY_REPO for public style skill.
- **Role:** visual-board/deck work with explicit layout/style defaults and human selection.
- **Durable lesson:** taste/quality guidance can be reusable, while the human remains the final selection gate.

## Notion Full Control
- **Source state:** EXACT at integration-pattern level + EXACT_PRIMARY_REPO.
- **Role:** search, retrieve, query, create/update pages and append blocks through a local Notion API wrapper when connector capabilities are insufficient.
- **Credential pattern:** environment variable first, then macOS Keychain.
- **Durable lesson:** systems-of-record can be wrapped behind exact tooling while the skill handles schema inspection and workflow decisions.

## Typefully Control
- **Source state:** EXACT as source example + EXACT_PRIMARY_REPO.
- **Role:** inspect/manage social sets, drafts, queue, analytics, media and publishing via the Typefully REST API.
- **Safety/default:** public skill instructs draft creation for tests unless live publishing is explicitly requested.
- **Durable lesson:** action tools should encode reversible test defaults and explicit live-action boundaries.

## Notion / Docs / calendar / email integrations broadly
- **Source state:** EXACT at interview pattern level.
- **Role:** reduce tab switching and let the agent create/update real records.
- **Durable lesson:** mature workflows should connect to the appropriate system of record/action rather than terminate as disposable chat output.

## Cloud agents / Slack-style interfaces
- **Source state:** EXACT as source discussion; product details subject to commercial bias and rapid change.
- **Role:** unattended or collaborative execution.
- **Durable lesson:** recurring workflows may need a cloud runtime rather than a local computer.

## Credential/security boundary
- **Evidence:** primary repo shows mixed hygiene. Several skills explicitly use environment variables or Keychain, while one public YouTube helper contains hardcoded default API credentials.
- **Rule for reuse:** do not copy exposed credentials or treat public defaults as secrets. Golfkuponger credentials must stay in managed connector authentication, environment variables, OS keychain or a dedicated secret store.

## Golfkuponger implementation note
Do not copy Riley's exact tool stack by default. Reuse the mechanism and choose the simplest available tool that satisfies the workflow, permissions, reliability and cost requirements.
