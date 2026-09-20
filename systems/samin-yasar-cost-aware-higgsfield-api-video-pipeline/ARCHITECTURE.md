# Architecture

Human or agent brief
→ Story and shot planner
→ Preview/reference image generation
→ Cost-aware model router
→ Lower-cost draft video models
→ Selection gate
→ Premium/final model or transformation
→ Output QA
→ Generation ledger and learning record

Optional after repetition is proven:
→ reusable skill
→ application wrapper

## Provenance

Story planning, preview images, cheaper drafts, selecting a winner and premium finishing are EXACT from the source at 13:03–14:26.

Turning those actions into an explicit router, lifecycle state machine and persistent ledger is RECONSTRUCTED.

The source's packaging into a skill and microsite is EXACT as a concept at 14:32–17:53. Making packaging conditional on proven repeated use is RECONSTRUCTED.

## Recommended state model

DRAFT → PREVIEWED → DRAFT_RUNNING → DRAFT_READY → SELECTED → PREMIUM_RUNNING → REVIEW → ACCEPTED / REJECTED / FAILED.

The labels are RECONSTRUCTED. Each paid transition should carry a budget authorization and a cost/status record.
