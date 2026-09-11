# Architecture

## Source-backed layers
1. **Truth inputs:** communication goal, approved copy, authentic product/UI media and destination.
2. **Reference layer:** a suitable source film, its complete archived prompt and separate adaptation guide.
3. **Assistant layer:** resolve scene sequence, timing, transitions, audio, exact-copy list and minimal reference roles.
4. **Action boundary:** drafting and review do not authorize uploads or generation. Check capabilities and prices through read-only operations.
5. **Production adapter:** the creator package uses Higgsfield MCP. Current provider guidance prefers CLI for coding agents; a CLI port is a separate adaptation, not presumed compatibility.
6. **Model and job state:** one full-film request; save actual model/settings, input identifiers, job ID and status. Rejoin uncertain jobs instead of duplicating them.
7. **Review and bounded correction:** inspect playback and audio; compare with intended communication and exact content; one corrective generation or supported edit by default.

Layers 2–7 are directly supported by the inspected creator instructions and provider documentation. Maintaining business truth separately is an architectural synthesis; it must not be confused with a demonstrated integration.

## State contract — RECONSTRUCTED
`draft → approved → submitted → completed → reviewed → accepted/rejected`

These are proposed record states, not an observed provider API enum. A completed job is not necessarily an accepted deliverable. Preserve failed attempts, corrections and costs. Suggested record: source URL/hash, adapted prompt, exact copy, asset roles, settings, job ID, status, observed defects and final decision. The source explicitly requires much of this record; the lifecycle names are our reconstruction.

See SOURCE_MAP.md: R1–R3 and H1–H3.
