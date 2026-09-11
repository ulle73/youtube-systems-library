# Architecture

## Components
1. **Human client** - conventional web UI for people.
2. **Agent clients** - Claude, Codex, GrokBot or other assistants.
3. **Agent-facing application interface** - portable skill/instructions defining how an agent authenticates and operates the app.
4. **Application operations** - create, move, edit, delete, comment and related business actions.
5. **Shared realtime state** - one durable database visible to every client; Convex is the demonstrated implementation.
6. **Identity and attribution** - records whether a human or agent performed an action.
7. **Deployment layer** - GitHub source plus Vercel hosting in the demonstration.

## Data flow
`human or agent intent`
-> `bounded application action`
-> `backend validation/mutation`
-> `shared durable state`
-> `realtime update to connected clients`
-> `attributed UI/event`

## Coordination model
Agents do not need direct peer-to-peer communication. The application state becomes the coordination substrate: each actor reads current truth, performs an allowed mutation, and leaves observable state for the next actor.

## Identity warning
The source shows an important failure mode: sharing one agent configuration can collapse several agent sessions into one displayed identity. Production design therefore needs separate principals or delegated scoped identities when actor-level attribution matters.

## Golfkuponger adaptation boundary
For future internal systems, mutable company truth should remain in the maintained backend/source of truth. Skills and agents should consume and mutate that state through explicit operations rather than copying authoritative state into prompts or memories.
