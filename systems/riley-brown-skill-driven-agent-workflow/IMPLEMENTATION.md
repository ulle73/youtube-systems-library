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

## Composition design

Prefer primitives with clean responsibility boundaries. Example:
- research/retrieval skill;
- evidence extraction skill;
- visual structuring skill;
- drafting skill;
- system-write/persistence skill.

A composite workflow can orchestrate these without duplicating each primitive's internal instructions. The source explicitly supports skill mix-and-match; the interface discipline is an adaptation for maintainability.

## Review escalation

Do not use the same QA standard for every skill.

- Low blast radius: human outcome review may be sufficient during iteration.
- Medium blast radius: inspect critical instructions and tool permissions; require visible review or rollback.
- High blast radius: audit skill contents, inputs, credentials/permissions, external actions and failure behavior; require independent approval where appropriate.

## Deployment

Keep skill logic portable where possible. Interactive/local execution and cloud/unattended execution are separate deployment choices. A workflow that becomes recurring may later be moved to a cloud runner, but only after its behavior and permission boundaries are understood.

## Not established by the source
- exact file format for Riley's skills;
- version numbering convention;
- formal automated test harness;
- pass/fail count required before promotion;
- rollback process;
- permission schema for production agents.

Do not invent these as Riley's implementation. They should be designed separately if Golfkuponger needs them.
