# Architecture

## Components

1. **Real work surface** — the actual task and current material/context.
2. **Human outcome standard** — the operator's judgment of what good looks like.
3. **Skill primitive** — reusable procedure, decision criteria and tool protocol.
4. **Execution agent** — runs the primitive against current context.
5. **Feedback loop** — observed failure becomes instruction/process revision.
6. **Fresh-context test** — verifies the primitive without hidden conversational carryover.
7. **Composition layer** — combines stable primitives into higher-order workflows.
8. **Risk/permission gate** — determines review and autonomy based on consequence and reversibility.
9. **Execution environment** — interactive/local or unattended/cloud depending on runtime needs.

## Data flow

`task + current context + outcome standard`
→ `agent executes skill`
→ `candidate output`
→ `human/eval judgment`
→ if weak: `failure feedback → skill update → fresh-context rerun`
→ if stable: `promote/reuse primitive`
→ optionally `compose with other primitives`
→ `risk gate`
→ `interactive action or cloud automation`

## Boundary with company truth
The source does not explicitly present a formal company-state architecture. For Golfkuponger, use the existing Research Library principle that mutable business facts remain in maintained sources and are loaded at runtime rather than copied into durable skill instructions. This adaptation is **RECONSTRUCTED from combined evidence**, not an EXACT Riley implementation detail.

## Human control points
- define outcome/quality standard;
- select among creative options;
- reject weak outputs and explain failure;
- decide when a repeated procedure deserves promotion to a skill;
- approve higher-risk external actions;
- retire or revise stale/unused skills.
