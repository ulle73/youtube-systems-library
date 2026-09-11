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
- **Source:** https://www.youtube.com/watch?v=3cYTWLdHgAE
- **Creator:** Riley Brown
- **Category:** agentic-workflow-design / skill-engineering
- **Status:** RECONSTRUCTED
- **Capture:** transcript-backed + primary public skill-repository corroboration; partial multimodal; preferred Apify transcript retrieval remained blocked by account hard limit
- **Core lifecycle:** real work -> useful repetition -> skill -> outcome test -> failure feedback -> skill update -> fresh-context retest -> composition -> risk gate -> local/cloud execution
- **Implementation architecture:** skill instructions/orchestration -> scripts/CLIs/other skills -> APIs/tools -> artifacts/state -> human review
- **Primary corroboration:** Riley's public `rileys-skills` repository; especially concrete composition in `youtube-thumbnail`, which reuses YouTube research + internet asset retrieval + image generation
- **Strongest video evidence:** bottom-up skill creation (19:04–19:16), skill composition (31:15–31:55), fresh-context outcome loop (32:08–33:07), risk-dependent review (33:23–33:45), local/cloud split (34:53–37:58)
- **Security finding:** one public helper contains hardcoded default API credentials; values are intentionally excluded and must not be reused
- **Unresolved:** formal reliability threshold, version/rollback protocol, automated eval suite, large-scale composition reliability, private/local skill details, frame-level UI details
- **Raw evidence:** stored separately in Google Drive Systems Library / Evidence

When answering future questions about creating, refining or composing AI skills/workflows, treat this as a source-backed operating model. Prefer its bottom-up promotion rule, deterministic-tool boundary and fresh-context retest loop over speculative skill-library design. Prefer small composable primitives with explicit dependencies, and preserve stricter audit requirements for high-blast-radius work.
