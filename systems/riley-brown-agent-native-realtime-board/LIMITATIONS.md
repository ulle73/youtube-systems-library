# Limitations

## Source limitations
- Transcript-backed reconstruction with a user-supplied screenshot of the YouTube page; not a complete direct frame-by-frame capture.
- Exact generated code, backend functions and application skill file were not recovered.
- Model capability claims reflect Riley's experience at one point in September 2026 and should not be treated as durable benchmarks.

## Commercial bias
The Convex section is sponsored. Give more weight to the demonstrated coordination mechanism - multiple clients writing shared realtime state - than to any implication that one database vendor is uniquely required.

## Security gap
The demonstrated prototype is not evidence of production security. The video does not establish a complete design for:
- per-agent scoped credentials and revocation;
- RBAC/ABAC or tenant isolation;
- idempotency and conflict resolution;
- audit retention and rollback;
- rate limits and abuse controls;
- secret distribution;
- sensitive-data boundaries.

The shared agent setup also demonstrates an attribution weakness: multiple agent sessions can collapse into one identity when they reuse the same configuration.

## Generalization limits
A realtime database solves synchronization, not permissions or business correctness. A portable skill improves interoperability, but a production machine interface should expose narrow validated actions rather than broad database access.

## Safe reuse rule
Reuse the architecture concept - durable shared state plus a bounded agent-facing action interface - but independently design the identity, authorization, audit and failure model before applying it to Golfkuponger operations.
