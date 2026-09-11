# Source Map

Primary source: https://www.youtube.com/watch?v=3cYTWLdHgAE
Capture: user screenshot + public timestamped transcript/breakdown; partial multimodal.

| Time | Evidence | State |
|---|---|---|
| 02:44-04:10 | Defines an agent-native Trello-style board for human and agent users with attributed actions | EXACT |
| 04:10-07:30 | Build brief covers platform, reference app, user flow, design direction and database choice | EXACT |
| 07:30-08:47 | Convex is used as the realtime shared state layer; sponsor segment | EXACT |
| 08:47-12:00 | Generated schema/tables and a real user write are inspected directly | EXACT |
| 12:00-14:43 | App-specific skill is installed in GrokBot and used to write to the live board | EXACT |
| 12:26-12:46 | Shared agent setup collapses distinct bot actions into a common displayed agent identity | EXACT |
| 14:43-19:14 | QA categories: function, layout, mobile, data/realtime, edge-case testing, security; fixes are revised in a batch | EXACT |
| 19:14-21:41 | Same interface is exercised from another agent and another human account; a formatting bug is surfaced | EXACT |
| 21:41-23:00 | Source is put on GitHub and deployed through Vercel | EXACT |
| 23:06-24:45 | Deployed board is reorganized/populated using the operator's real business context | EXACT |

## Reconstructed architecture
`human UI + agent clients -> app-specific action interface -> backend operations -> shared realtime state -> attributed events -> synchronized clients`

The source demonstrates the individual layers but does not state this exact chain as a named architecture.

## Evidence caveats
- Convex is sponsored; separate the shared-state mechanism from claims of product superiority.
- Full video frame capture was not completed.
- Exact agent skill contents, credentials and backend API contract were not captured.
- The prototype does not demonstrate production-grade authorization, tenancy, idempotency, audit or load behavior.
