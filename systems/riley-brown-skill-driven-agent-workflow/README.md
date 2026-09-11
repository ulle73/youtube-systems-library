# Riley Brown Skill-Driven Agent Workflow

## Purpose
A source-backed operating model for growing reusable AI capability from real work rather than designing a speculative library of agents and skills up front.

## Core idea
Do the task first. When a useful procedure repeats, capture it as a skill. Run the skill on representative work, judge the outcome, revise it from observed failures, then retest from fresh context. Once primitives are stable, combine them into larger workflows. Increase inspection, permission controls and human approval as blast radius rises.

## Canonical loop
`real work -> useful repetition -> skill -> outcome test -> feedback -> update -> fresh-context retest -> stable primitive -> composition -> risk gate -> local/cloud execution`

## Implementation model
Primary public repo evidence shows that Riley's skills are not merely saved prompts. They are filesystem-backed operational packages that can contain:
- skill instructions for triggers, workflow, defaults and decision rules;
- scripts/CLIs for exact retrieval, API calls and artifact generation;
- references/templates/assets;
- external service integrations;
- local working files and manifests.

A useful shorthand is:

`skill/orchestration -> script or CLI -> API/tool -> artifact/state -> human review`

The exact split varies by skill, but the durable principle is to keep judgment/orchestration reusable while delegating exact repeatable mechanics to deterministic components where that improves reliability.

## Concrete composition evidence
Riley's public `youtube-thumbnail` skill explicitly composes narrower capabilities: `youtube-researcher` for reference discovery, `internet-image-puller` for supporting assets, and image generation for final outputs. This confirms that skill composition is implemented as dependency reuse rather than only discussed conceptually.

## Why it matters
This system provides a concrete lifecycle for reusable agent capabilities:
- skill demand is proven by actual repeated work;
- skill quality is tested against outcomes rather than instruction aesthetics alone;
- fresh context reduces false confidence caused by conversational carryover;
- small capabilities can compound through composition;
- exact mechanics can be moved into scripts/CLIs while the skill keeps higher-level judgment;
- human judgment remains explicit for taste, novelty and risk;
- deployment is separated from workflow logic;
- credentials remain runtime configuration, not reusable skill knowledge.

## Source status
**RECONSTRUCTED — transcript-backed + primary public repo corroboration; partial multimodal.** The critical workflow mechanics are directly stated in transcript evidence and several implementation details are corroborated by Riley's public `rileys-skills` repository. Direct frame-by-frame capture of the full video was not completed, so UI-specific details remain unresolved unless separately verified.

## Security note
The public repository shows mixed credential hygiene: several skills use environment variables or OS keychain storage, while one public YouTube helper contains hardcoded default API credentials. Those values are intentionally not preserved here and must not be reused. Golfkuponger implementations should use managed connector authentication, environment variables, keychain or a dedicated secret store.

## Use at Golfkuponger
When a repeated AI-assisted job appears, search for an existing skill/system first. If none fits, solve the task well before formalizing it. Promote the proven procedure into a small reusable skill, test it in fresh context, refine it from failures and only then compose or automate it. Put exact repeatable operations in tools/scripts when useful, keep mutable business truth outside durable skill instructions, and never apply the low-risk creative evaluation standard to payments, customer-impacting writes, compliance-sensitive actions or destructive operations.

## Evidence
- Source: https://www.youtube.com/watch?v=N34zz1-RSGw
- Primary implementation corroboration: https://github.com/rbrown101010/rileys-skills
- Drive evidence: `GOLFKUPONGER/Systems Library/Evidence/2026-08-16_riley-brown_skill-driven-agent-workflow_evidence.md`
- Research topic: `GOLFKUPONGER/Research Library/Topics/Agentic Workflow Design/`
