# Tools and dependencies

| Tool | Role in system | Evidence/status |
|---|---|---|
| refero.design | Discover strong reference sites | EXACT, ~01:00 |
| Mintlify | Example gold-standard reference chosen by Jack | EXACT/corroborated |
| Relume | Sitemap, wireframes, style guide, HTML export | EXACT, 01:55–04:19 |
| Design Loop | Multi-critic design iteration | EXACT dependency; internals cross-source |
| Higgsfield | Images/video/logos connected to Claude | EXACT, 05:42–09:22 |
| Savee | Visual/UI inspiration | EXACT, ~09:42 |
| SlopMonster | AI-copy quality loop | EXACT linked repo: https://github.com/ItsssssJack/SlopMonster |
| 21st.dev | UI component source | EXACT, ~19:03 |
| Flaticon | Icon source | EXACT, ~19:56 |
| Icons8 | Icon source | EXACT, ~19:56 |
| IconScout | Icon source | EXACT, ~19:56 |
| Mobile optimization repo | Dedicated mobile QA/optimization | EXACTly referenced, identity UNRESOLVED |
| Claude SEO repo | SEO research/strategy skill | EXACTly referenced, identity UNRESOLVED |
| Glaido | Example business/keyword target in SEO demo | EXACT example |
| GitHub | Code/version source; Jack specifies private repo | EXACT, ~22:14 |
| Vercel | Deployment | EXACT, ~22:14 |

## SlopMonster dependency — source-backed implementation

The linked repo implements a concrete gate:

`lint (5-point deterministic rules) -> three-pass rewrite -> cleanse with a rival model family -> re-lint -> ship only when clean`

It also explicitly warns not to invent proof. This is stronger evidence than a verbal mention because the video links to the maintained implementation repository.

## Design Loop dependency

The current video installs/uses the Design Loop skill but doesn't reveal all of its instructions. A separate same-creator tutorial describes fresh-context critics for:
- brief compliance;
- design-system alignment;
- rendered craft/quality.

Cross-source details must stay labeled `RECONSTRUCTED`.
