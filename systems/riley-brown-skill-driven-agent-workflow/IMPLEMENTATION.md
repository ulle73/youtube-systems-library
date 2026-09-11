# Implementation

## Minimal implementation pattern

A reusable skill based on this system should contain enough durable information that a fresh agent context can execute the task without relying on the conversation that originally created it.

Recommended fields:
- objective;
- trigger / when to use;
- required inputs;
- ordered procedure or decision logic;
- tools/data sources;
- expected output and quality standard;
- risk/approval boundary;
- known failure modes;
- examples only where they clarify the outcome.

This field structure is a **Golfkuponger adaptation**, not an EXACT Riley file schema.

## Primary-repo implementation lesson
Riley's public repository shows that a mature skill can include more than prose instructions. Portable skill packages may contain:
- `SKILL.md` instructions;
- helper scripts;
- references;
- templates/assets;
- metadata;
- explicit output/artifact conventions.

The strongest reusable implementation split is:

`durable orchestration + judgment rules`
→ `deterministic script/CLI/tool for exact mechanics`
→ `external API/service or local executable`
→ `structured artifact/state`
→ `human/eval judgment`

Do not force exact mechanics into free-form model reasoning when a small script, CLI or typed tool can make them cheaper, more repeatable or safer.

## Promotion gate

Create/promote a skill when all are true:
1. the job has occurred in real work;
2. a useful procedure has been demonstrated;
3. the procedure is likely to repeat;
4. the desired outcome can be judged;
5. the reusable method can be separated from one-off task context.

The bottom-up principle is EXACT; this five-part gate is RECONSTRUCTED for operational use.

## Refinement loop

For low-risk knowledge/creative skills:
1. execute in a representative case;
2. compare output to the operator's quality standard;
3. feed concrete failure feedback to the agent;
4. revise the skill;
5. restart from fresh context;
6. rerun;
7. preserve meaningful failure lessons in the skill rather than relying on remembered chat context.

The run/feedback/update/fresh-context loop is source-backed. Persisting explicit failure lessons is RECONSTRUCTED.

## When to introduce a helper script or CLI
A helper implementation is a strong candidate when the operation has one or more of these traits:
- exact API parameters or schemas;
- repeated normalization/transformation logic;
- retry/rate-limit behavior;
- file naming/deduplication/manifests;
- deterministic artifact generation;
- credential lookup/configuration;
- repeatable validation checks.

This criterion is RECONSTRUCTED from Riley's public implementations. Examples include the YouTube research helper, image-pulling helper, Notion API wrapper and Typefully CLI.

## Composition design

Prefer primitives with clean responsibility boundaries. Source-backed examples include:
- YouTube research/retrieval;
- internet image/asset retrieval;
- Excalidraw diagram generation;
- system-of-record/API control;
- thumbnail generation as a higher-order composite.

A composite workflow should orchestrate existing primitives without duplicating their internal instructions or code.

### Primary implementation example: YouTube Thumbnail
Riley's public `youtube-thumbnail` skill declares these dependencies:
1. `youtube-researcher` for style/reference thumbnail discovery;
2. `internet-image-puller` for logos/supporting assets when needed;
3. image generation/editing for final 16:9 variants;
4. final existence/dimension verification.

This is EXACT_PRIMARY_REPO evidence for composition by dependency reuse.

### Interface discipline for reusable primitives
For Golfkuponger, define for each primitive:
- trigger;
- inputs;
- outputs/artifacts;
- dependencies;
- failure behavior;
- approval boundary.

The source supports composition; this explicit interface contract is an adaptation for maintainability and reliable orchestration.

## System-of-record/action wrappers
Primary repo examples support a useful pattern:
- inspect configuration first;
- inspect schema/state before writing;
- use narrow high-level commands for common actions;
- expose a raw/API fallback for uncovered operations;
- default tests toward reversible actions where possible.

Examples:
- `notion-full-control` retrieves/searches/queries before exact page/block writes;
- `typefully-control` instructs draft creation for tests unless live publishing is explicitly requested.

The tools are examples; the durable rule is to make exact external actions explicit and reviewable.

## Artifact contracts
Some skills produce durable editable artifacts rather than only chat text. The public Excalidraw skill demonstrates:
1. plan the diagram as nodes/connectors/layout;
2. translate into structured Excalidraw JSON elements;
3. run a CLI to create the editable artifact;
4. generate a preview when supported;
5. export/share the result.

This suggests that output formats and validation steps belong in the skill contract when the work produces files or structured state.

## Review escalation

Do not use the same QA standard for every skill.

- Low blast radius: human outcome review may be sufficient during iteration.
- Medium blast radius: inspect critical instructions and tool permissions; require visible review or rollback.
- High blast radius: audit skill contents, inputs, credentials/permissions, external actions and failure behavior; require independent approval where appropriate.

## Credential handling
Credentials are runtime configuration, never reusable skill content.

Primary repo inspection shows mixed practices: some skills explicitly use environment variables or OS keychain storage, while one public helper contains hardcoded default API credentials. Treat public/default credentials as exposed and do not preserve or reuse their values.

Golfkuponger default hierarchy should be:
1. managed connector/plugin authentication where available;
2. dedicated secret store / platform credential management;
3. environment variable or OS keychain for local tooling;
4. never source-controlled plaintext secrets.

This hierarchy is a Golfkuponger safety adaptation, not Riley's stated universal rule.

## Deployment

Keep skill logic portable where possible. Interactive/local execution and cloud/unattended execution are separate deployment choices. A workflow that becomes recurring may later be moved to a cloud runner, but only after its behavior and permission boundaries are understood.

## Not established by the source
- exact file format used by every Riley skill;
- version numbering convention;
- formal automated test harness;
- pass/fail count required before promotion;
- rollback process;
- production permission schema;
- reliability of deeply nested or large-scale skill composition.

Do not invent these as Riley's implementation. They should be designed separately if Golfkuponger needs them.
