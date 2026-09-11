# Architecture

## Components

1. **Real work surface** — the actual task and current material/context.
2. **Human outcome standard** — the operator's judgment of what good looks like.
3. **Skill package** — reusable trigger logic, procedure, decision criteria, defaults and tool protocol.
4. **Deterministic execution layer** — scripts, CLIs or explicit tool calls for operations that benefit from exactness.
5. **External data/action layer** — APIs, connected systems and services used for retrieval, creation or updates.
6. **Local state/artifact layer** — working files, manifests, references, templates and editable outputs.
7. **Execution agent** — selects and runs the relevant skill against current context.
8. **Feedback loop** — observed failure becomes instruction/process revision.
9. **Fresh-context test** — verifies the primitive without hidden conversational carryover.
10. **Composition layer** — combines stable primitives into higher-order workflows by dependency reuse.
11. **Risk/permission gate** — determines review and autonomy based on consequence and reversibility.
12. **Execution environment** — interactive/local or unattended/cloud depending on runtime needs.

## Primary-repo implementation pattern
Riley's public skills materially support this layered model. The exact split differs by skill, but a common pattern is:

`SKILL.md / orchestration`
→ `script, CLI or narrower skill`
→ `API / service / local executable`
→ `file, manifest, draft, diagram or other artifact/state`
→ `human judgment or next composed skill`

Examples:
- `youtube-researcher` → local Python helper → SerpAPI/Supadata → structured search/transcript data → in-chat synthesis;
- `internet-image-puller` → helper script → SerpAPI/Firecrawl → downloaded assets + manifest → downstream visual workflow;
- `youtube-thumbnail` → `youtube-researcher` + `internet-image-puller` + image generation → thumbnail variants → human verification/selection;
- `excalidraw-diagrams` → structured element plan → Excalidraw JSON + CLI → editable `.excalidraw` artifact + preview/share URL;
- `typefully-control` / `notion-full-control` → local API wrappers → external system records/actions.

This supports a stronger interpretation of skills as **orchestration packages around exact capabilities**, rather than monolithic prompts that ask the model to improvise every operation.

## Data flow

`task + current context + outcome standard`
→ `agent selects skill package`
→ `skill invokes scripts/tools/APIs or other skills as needed`
→ `candidate artifact/action/output`
→ `human/eval judgment`
→ if weak: `failure feedback → skill update → fresh-context rerun`
→ if stable: `promote/reuse primitive`
→ optionally `compose with other primitives`
→ `risk gate`
→ `interactive action or cloud automation`

## Composition boundary
Composition should reuse a primitive's public responsibility rather than duplicate its internals. The `youtube-thumbnail` skill is direct primary-repo evidence: it depends on narrower research and asset-retrieval skills, then adds thumbnail-specific orchestration and generation rules.

A composable primitive benefits from:
- clear trigger / intended job;
- explicit required inputs;
- predictable outputs or artifacts;
- bounded responsibility;
- explicit tool/service dependencies;
- known failure and review behavior.

The source demonstrates composition; this interface discipline is RECONSTRUCTED for reliable reuse.

## Boundary with company truth
The source does not explicitly present a formal company-state architecture. For Golfkuponger, use the existing Research Library principle that mutable business facts remain in maintained sources and are loaded at runtime rather than copied into durable skill instructions. This adaptation is **RECONSTRUCTED from combined evidence**, not an EXACT Riley implementation detail.

## Credential boundary
Credentials are not part of durable workflow knowledge. Primary repo inspection shows both safer patterns (environment variables / macOS Keychain) and one unsafe pattern (hardcoded default API credentials in a public helper). The latter is evidence of a security flaw, not a pattern to reproduce.

For Golfkuponger:
`skill/tool definition != secret`

Use managed connector auth, environment variables, keychain or a dedicated secret store and keep source-controlled skill content credential-free.

## Human control points
- define outcome/quality standard;
- select among creative options;
- reject weak outputs and explain failure;
- decide when a repeated procedure deserves promotion to a skill;
- approve higher-risk external actions;
- decide whether a deterministic operation belongs in a script/tool rather than model improvisation;
- retire or revise stale/unused skills.
