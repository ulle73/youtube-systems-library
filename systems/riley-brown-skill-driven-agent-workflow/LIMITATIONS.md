# Limitations

## Evidence limitations
- Primary Apify transcript retrieval was still blocked on 2026-09-11 by the connected account's monthly usage hard limit.
- The video reconstruction is based on public transcript sources with timestamp anchors, not a complete direct frame-by-frame capture.
- Riley's public `rileys-skills` repository now corroborates several exact skill files, helper patterns and dependencies, but it cannot verify private/local skills or every UI detail shown in the video.
- Tool-specific behavior may change faster than the durable workflow principles.

## What primary-repo corroboration improves
The public repository materially strengthens confidence in:
- filesystem-backed skill packages under a personal Codex skills directory;
- skills containing instructions plus scripts/references/assets/metadata where useful;
- YouTube research separated into SerpAPI search, Supadata transcript/metadata retrieval and agent synthesis;
- image retrieval as a separate reusable primitive;
- explicit dependency composition in the YouTube thumbnail workflow;
- structured artifact generation through Excalidraw JSON + CLI;
- local wrappers around Notion and Typefully APIs.

These implementation details may be treated as `EXACT_PRIMARY_REPO`. They do not make unobserved video UI details frame-verified.

## Security limitation / finding
Primary repo inspection shows mixed credential hygiene. Several public skills use environment variables or macOS Keychain patterns, but one public YouTube helper contains hardcoded default API credentials. The credential values are intentionally not preserved in this Systems Library and must be treated as exposed/compromised rather than reusable configuration.

Golfkuponger must not copy credentials from public repositories. Keep secrets in managed connector authentication, a dedicated secret store, environment variables or OS keychain as appropriate.

## Source bias
Riley discusses products and services with which he is commercially involved. Give more weight to directly demonstrated workflow mechanics and public implementation artifacts than to product-specific superiority, productivity or business-outcome claims.

## Generalization limits
- Creator/content workflows have a lower failure cost than many Golfkuponger operations.
- Outcome-only evaluation is not a sufficient control for payments, destructive writes, sensitive data, compliance-sensitive communication or production changes.
- Skill composition is demonstrated concretely at a practical small scale; reliability of large agent fleets or deeply nested skill composition is not established by this source.
- Specific Codex, cloud-agent and third-party integration capabilities can change quickly.

## Not established by the source
The following remain **INFERRED / unresolved** and must not be attributed to Riley as a demonstrated universal implementation:
- semantic versioning of skills;
- formal pass-rate thresholds;
- automated regression suites;
- rollback/deprecation protocol;
- production permission schema;
- exact multi-user agent architecture;
- exact contents of private/local Riley skills not present in the public repo;
- reliability limits for deeply nested skill chains.

## Safe reuse rule
Reuse the durable mechanics — bottom-up promotion, outcome refinement, fresh-context retesting, composable bounded primitives, deterministic tooling where useful, and risk-scaled review — but re-evaluate current tools, permissions, credentials and deployment choices for the actual Golfkuponger workflow before implementation.
