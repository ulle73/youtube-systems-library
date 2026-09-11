# Prompt Patterns

These are reusable **RECONSTRUCTED prompt patterns**, not verbatim source prompts unless explicitly marked.

## Promote proven work into a skill
**Source mechanism: EXACT** — Riley describes having the agent turn useful repeated work into a skill.

> Turn the procedure we just used successfully into a reusable skill. Preserve the durable steps, decision rules, tools, expected output and important failure lessons. Do not hardcode one-off task context that will change next time.

## Refine from a failed outcome
**Source mechanism: EXACT** — Riley describes explaining what was wrong and having the skill updated.

> The result from this skill was weak in these specific ways: [failures]. Update the skill so those failures are less likely next time without overfitting to this single example.

## Fresh-context regression test
**Source mechanism: EXACT** — Riley explicitly recommends restarting in fresh context before retesting.

> Use the skill on this task using only the information available in this fresh context. Produce the normal output without relying on prior conversations.

## Compose existing skills
**Source mechanism: EXACT** — Riley describes mixing and matching skills into new workflows.

> Before creating a new end-to-end skill, identify which existing proven skills can be composed to solve this task. Keep each primitive responsible for its own part and define the handoff between them.

## Risk review before promotion to automation
**Source principle: EXACT; prompt structure: RECONSTRUCTED.**

> Review this workflow before it is allowed to act automatically. Identify external writes, sensitive data, payment/destructive actions, irreversible steps, permission scope, failure modes, rollback options and where human approval is required.

## Outcome review
**RECONSTRUCTED.**

> Evaluate the output against the intended outcome rather than the elegance of the instructions. State what succeeded, what failed, whether the failure is systematic or case-specific, and what skill change would most improve the next fresh-context run.
