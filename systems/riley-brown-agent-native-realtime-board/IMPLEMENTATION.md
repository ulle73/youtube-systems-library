# Implementation

## Minimum product contract
A reusable implementation needs four explicit contracts:
- **identity:** who is acting - human, agent, owner/delegator;
- **actions:** what operations can be performed;
- **state:** where authoritative records live;
- **events/attribution:** how changes become visible and traceable.

## Agent-facing interface
The source packages app access into a portable skill that can be installed in different assistants. For production reuse, the skill should contain procedure and endpoint/tool guidance, while credentials remain external runtime configuration.

Recommended interface fields:
- application identity and environment;
- authentication/bootstrap procedure;
- supported actions and required arguments;
- read-before-write requirements;
- attribution rules;
- validation/idempotency behavior;
- error handling;
- permissions and approval boundaries.

This explicit contract is RECONSTRUCTED for safer reuse; the exact source skill file was not captured.

## Shared-state rule
Keep authoritative work in one backend. Different agents should retrieve current state before meaningful mutations instead of relying on stale chat memory. Realtime transport is useful but not sufficient; consistency, authorization and conflict handling remain separate concerns.

## Validation pattern
Do not accept a rendered UI as proof. Verify:
1. schema/data model;
2. human write -> stored record;
3. agent write -> stored record;
4. attribution;
5. second-client visibility;
6. failure behavior with malformed/edge-case input.

## Production hardening missing from source
- separate, scoped agent tokens;
- token rotation/revocation;
- RBAC/ABAC;
- idempotency keys;
- concurrency/conflict policy;
- complete audit/event log;
- rollback/recovery;
- rate limits and abuse controls;
- environment separation and secret management.
