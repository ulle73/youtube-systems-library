# Riley Brown Agent-Native Realtime Board

## Purpose
A source-backed reconstruction of a business application designed for both people and AI agents as first-class users.

## Core idea
Do not make one AI assistant the owner of shared operational state. Put durable state in the application, expose bounded actions to agents, and let humans and agents from different platforms operate the same records with attribution.

## Canonical architecture
`human UI + agent clients -> app-specific action interface -> backend operations -> shared realtime state -> attributed updates -> all clients`

The demonstrated stack uses Claude Code/Fable 5.1 for construction, Convex for realtime state, an application skill for agent access, and GitHub/Vercel for deployment. These products are examples; the durable pattern is provider-neutral.

## Build and validation loop
`five-part brief -> first-pass build -> inspect backend -> human write test -> agent write test -> six-point QA -> batch fixes -> second-agent test -> second-human realtime test -> deploy`

## Source status
**RECONSTRUCTED.** The workflow is backed by a timestamped public transcript/breakdown and the user's screenshot of the actual YouTube page. Full direct frame-by-frame capture was not completed. Convex is a sponsor in the source.

## Reuse rule
Treat the shared state and action contract as the stable center. Re-evaluate model, database, hosting, authentication and secret-management choices for the actual system. Do not copy prototype credential patterns into production.

## Evidence
- Video: https://www.youtube.com/watch?v=3cYTWLdHgAE
- Drive evidence: `GOLFKUPONGER/Systems Library/Evidence/2026-09-09_riley-brown_agent-native-realtime-board_evidence.md`
- Research topic: `GOLFKUPONGER/Research Library/Topics/Agent-Native Application Architecture/`
