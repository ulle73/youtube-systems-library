# Workflow

## Phase 1 - Define the product
1. Define the shared job humans and agents must perform.
2. Treat agents as first-class users with explicit attribution requirements.
3. Write the five-part build brief: platform, reference app, user flow, design direction, database/state choice.

## Phase 2 - Generate and verify the first pass
4. Ask the coding agent to build the initial application.
5. Inspect the generated backend schema/state directly.
6. Create a human account and verify a real persisted write.
7. Inspect the generated agent-facing skill/interface before relying on it.

## Phase 3 - Prove agent interoperability
8. Install the application interface in a second agent client.
9. Perform a minimal test mutation and verify it appears in shared state/UI.
10. Check attribution; detect whether shared credentials collapse distinct agents into one identity.
11. Run a realistic agent task against current business context.

## Phase 4 - Structured QA
12. Check Function.
13. Check Layout.
14. Check Mobile.
15. Check Data / realtime behavior.
16. Test edge cases.
17. Check Secure.
18. Batch related findings into a revision prompt when useful, then retest.

## Phase 5 - Cross-client testing
19. Install/use the same application interface from another AI platform.
20. Exercise comments, creation and edits; treat formatting/protocol failures as interface bugs.
21. Create another human account and verify that its changes appear without manual refresh.

## Phase 6 - Deploy and operationalize
22. Put source under GitHub.
23. Deploy through the configured hosting path (Vercel in the source).
24. Verify the public/team URL.
25. Populate or reorganize the application from real operational context.

## Production gate
The source stops at a working prototype. Before production, separately design scoped authentication, authorization, secrets, idempotency, audit events, rollback, concurrency controls, rate limits and sensitive-data rules.
