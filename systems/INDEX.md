# Systems Library Index

Search this index first, then inspect each system's `system.yaml`, `SOURCE_MAP.md`, and `LIMITATIONS.md` before reuse.

## System #001 — Seven-Level Claude Website Conversion Workflow

- **Path:** `systems/jack-roberts-seven-level-converting-website/`
- **Source:** https://www.youtube.com/watch?v=pUu4G2lINnk
- **Creator:** Jack Roberts
- **Category:** website-design-conversion
- **Status:** RECONSTRUCTED
- **Capture:** transcript + oEmbed; direct YouTube video/frames blocked by anti-bot; independent timestamped storyboard used as secondary corroboration
- **Core stack:** refero.design, Relume, Claude, Design Loop, Higgsfield, Savee, SlopMonster, 21st.dev, icon libraries, SEO skill, GitHub, Vercel
- **Core sequence:** reference -> sitemap -> wireframes/style -> Claude build -> critique -> assets -> interactive conversion element -> mobile QA -> copy QA -> UI polish -> SEO -> deploy
- **Strong linked implementation:** SlopMonster — https://github.com/ItsssssJack/SlopMonster
- **Unresolved:** exact mobile optimization repo; exact Claude SEO repo
- **Raw evidence:** stored separately in Google Drive Systems Library / Evidence

When answering future website-system questions, treat this as a source-backed implementation candidate rather than generic model advice. Preserve its EXACT / RECONSTRUCTED / INFERRED distinctions when adapting it.

## System #002 — Riley Brown Skill-Driven Agent Workflow

- **Path:** `systems/riley-brown-skill-driven-agent-workflow/`
- **Source:** https://www.youtube.com/watch?v=N34zz1-RSGw
- **Creator:** Riley Brown
- **Category:** agentic-workflow-design / skill-engineering
- **Status:** RECONSTRUCTED
- **Capture:** transcript-backed + primary public skill-repository corroboration; partial multimodal
- **Core lifecycle:** real work -> useful repetition -> skill -> outcome test -> failure feedback -> skill update -> fresh-context retest -> composition -> risk gate -> local/cloud execution
- **Implementation architecture:** skill instructions/orchestration -> scripts/CLIs/other skills -> APIs/tools -> artifacts/state -> human review
- **Primary corroboration:** Riley's public `rileys-skills` repository
- **Unresolved:** formal reliability threshold, version/rollback protocol, automated eval suite, large-scale composition reliability, private/local skill details, frame-level UI details
- **Raw evidence:** stored separately in Google Drive Systems Library / Evidence

When answering future questions about creating, refining or composing AI skills/workflows, treat this as a source-backed operating model. Prefer its bottom-up promotion rule, deterministic-tool boundary and fresh-context retest loop over speculative skill-library design.

## System #003 — Riley Brown Agent-Native Realtime Board

- **Path:** `systems/riley-brown-agent-native-realtime-board/`
- **Source:** https://www.youtube.com/watch?v=3cYTWLdHgAE
- **Creator:** Riley Brown
- **Category:** agent-native-applications / multi-agent-coordination / realtime-operations
- **Status:** RECONSTRUCTED
- **Capture:** user-provided YouTube screenshot + public timestamped transcript/breakdown; partial multimodal
- **Core architecture:** human UI + agent clients -> app-specific action interface -> backend operations -> shared realtime state -> attributed events -> synchronized clients
- **Build framework:** platform -> reference app -> user flow -> design direction -> database/state choice
- **QA framework:** function -> layout -> mobile -> data/realtime -> edge cases -> secure
- **Demonstrated stack:** Claude Code/Fable 5.1, Trello reference model, Convex realtime backend, portable agent skill, GitHub, Vercel
- **Key lesson:** coordinate heterogeneous agents through one durable source of truth and bounded application actions rather than one vendor's chat context
- **Critical risk:** connectivity does not solve identity or authorization; the demo shows shared agent identity ambiguity and does not establish production-grade RBAC, secret scope, idempotency, audit or rollback
- **Raw evidence:** stored separately in Google Drive Systems Library / Evidence

When answering future questions about multi-agent internal tools, treat this as a source-backed architecture candidate. Prefer shared durable state plus explicit machine-facing actions, while designing identity, permissions, audit and secret handling separately for production.
