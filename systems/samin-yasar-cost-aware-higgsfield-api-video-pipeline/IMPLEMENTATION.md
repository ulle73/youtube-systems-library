# Implementation

Nothing in this reconstruction was deployed.

## Phase 1 — manual staged production
1. Capture brief and acceptance criteria.
2. Create storyboard and preview frames.
3. Select a lower-cost draft model from the current catalog.
4. Generate a bounded set of draft clips.
5. Select one direction.
6. Authorize one premium/final generation.
7. Record actual spend, attempts and acceptance.

## Phase 2 — thin Higgsfield API adapter
Current provider documentation describes an asynchronous pattern: submit to a model endpoint, receive request/status information, poll to completion and capture the result URL/state. Credentials should be stored server-side or in an approved secret store.

Minimum reconstructed job fields:
- job/request ID
- provider/model/version
- stage: draft or premium
- duration and resolution
- submitted timestamp
- terminal status
- actual charge if available
- attempt number
- accepted/rejected plus reason

## Phase 3 — routing skill
A reusable skill can enforce storyboard-first behavior, draft/premium role selection, spending ceilings, premium approval and ledger write-back. The source's Higgsfield API Studio demonstrates the concept at 07:45–07:53, but the complete internal prompt/code was not independently audited.

## Phase 4 — optional studio/app
The source references OpenHiggsfield. The independently inspected repository https://github.com/wide-trace/open-higgsfield uses a catalog-driven studio with server-side generation calls, status polling, media-role inputs and run history. Extending such a base is an option only if a real app surface is required.

Graduate to automation only after repeated evidence that the staged workflow reduces accepted-output cost, rejected premium attempts, active human time or turnaround without lowering publishable quality.
