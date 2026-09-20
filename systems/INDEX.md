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

## System #004 — Chase AI Reference-Led Motion Design

- **Path:** `systems/chase-ai-reference-led-motion-design/`
- **Source:** https://www.youtube.com/watch?v=eyDKoGU_vHk
- **Creator:** Chase AI
- **Category:** media-production-workflows
- **Status:** RECONSTRUCTED; no runtime production test
- **Capture:** exact-ID third-party timestamped transcript, partial frame inspection, primary creator repository and official provider documentation
- **Primary implementation:** https://github.com/cth9191/motion-design
- **Core sequence:** goal -> source example -> complete adapted brief -> minimal references -> explicit paid-action boundary -> one full-film job -> playback review -> bounded correction -> accepted-output record
- **Critical distinction:** gallery films are Higgsfield source examples, not a success sample generated by the package. Programmatic generation consumes credits even when manual website use has an unlimited allowance.
- **Unresolved:** account-specific price/access, MCP-to-CLI adaptation, exact UI/text fidelity, accepted-output unit cost and independent reproduction
- **Privacy:** this public entry stores generic source-backed methods only; private business assessments remain outside this repository.

When answering future media-workflow questions, reuse the reference adaptation, permission boundary and bounded-review contract. Do not promote a model label, gallery appearance or completed job into evidence of commercial value.


## System #005 — Cody AI OFM Synthetic Creator Funnel

- **Path:** `systems/cody-ai-ofm-synthetic-creator-funnel/`
- **Source:** https://www.youtube.com/watch?v=QRnjjpV_Ve4
- **Creator:** Cody AI OFM
- **Category:** creator-commerce-workflows
- **Status:** RECONSTRUCTED; no runtime production or commercial test
- **Capture:** exact video identity + complete YouTube auto-caption coverage through a fallback transcript actor; current Fanvue policy/help cross-check
- **Core sequence:** audience/persona -> rights/disclosure -> consistent batch creative -> hook/buildup/trigger/reaction/CTA -> tracked destination -> transparent onboarding -> human handoff -> conversion/retention measurement
- **Critical distinction:** source revenue and algorithm claims are not validated. Device/network anti-detection, platform-evasion, guardrail-bypass, unlicensed likeness use and deceptive-human identity tactics are deliberately excluded from the reusable implementation.
- **Unresolved:** independent conversion lift, cost per accepted asset, synthetic-vs-conventional creative advantage, tool privacy/reliability, platform-policy stability and disclosure effects on trust.
- **Privacy:** raw transcript/evidence remains in the private Research Library; this public entry stores only distilled source-backed system knowledge.

When answering future creator-commerce or synthetic-persona questions, reuse the measurable funnel and persistent-context patterns while preserving explicit rights, disclosure, human-handoff and compliance boundaries.


## System #006 — Samin Yasar Cost-Aware Higgsfield API Video Pipeline

- **Path:** systems/samin-yasar-cost-aware-higgsfield-api-video-pipeline/
- **Source:** https://www.youtube.com/watch?v=BTVpef58xMY
- **Creator:** Samin Yasar
- **Category:** media-production-workflows
- **Status:** RECONSTRUCTED; no runtime production or commercial test
- **Capture:** exact video identity + complete YouTube auto-caption transcript through fallback provider; no scene-frame archive; current Higgsfield API and OpenHiggsfield repository cross-check
- **Core sequence:** story → storyboard/reference images → lower-cost video drafts → select winner → premium final/transformation → cost/result write-back
- **Critical distinction:** pay-per-generation visibility and staged spending are reusable mechanisms; the source's 10x efficiency claim, one-off demo cost/speed and client-SaaS demand are not validated.
- **Primary implementation references:** https://higgsfield.ai/higgsfield-api and https://github.com/wide-trace/open-higgsfield
- **Unresolved:** accepted-output unit cost, draft-to-final predictive value, output fidelity, account-specific break-even versus subscription, maintenance burden and commercial impact.
- **Privacy:** raw transcript/evidence remains in private Drive evidence; this public entry stores only distilled source-backed system knowledge.

When answering future AI-video production questions, reuse the progressive-spend pattern and generation ledger before proposing a new platform. Treat model names and promotional discounts as replaceable configuration, not durable architecture.
