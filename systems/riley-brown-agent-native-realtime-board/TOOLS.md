# Tools

## Claude Code / Fable 5.1
- **Source state:** EXACT as demonstrated construction environment.
- **Role:** generate, revise, inspect and deploy the application.
- **Reuse lesson:** model choice is replaceable; preserve the build/verification workflow rather than the September 2026 model ranking claim.

## Trello
- **Source state:** EXACT as reference product.
- **Role:** supplies a familiar board interaction/data mental model.
- **Reuse lesson:** a reference product can compress product intent when the desired behavior is genuinely similar.

## Convex
- **Source state:** EXACT; sponsored segment.
- **Role:** backend/shared realtime database in the demonstrated implementation.
- **Reuse lesson:** one shared durable state layer can coordinate humans and agents. Convex is an example, not a required architecture choice.

## Application skill / agent interface
- **Source state:** EXACT at the mechanism level; exact file contents unresolved.
- **Role:** lets GrokBot, ChatGPT/Codex and other agents operate the same app.
- **Reuse lesson:** expose machine-facing application actions through a portable, bounded interface.

## GitHub
- **Source state:** EXACT.
- **Role:** source repository before public deployment.

## Vercel
- **Source state:** EXACT.
- **Role:** host the web application after one-time configuration.
- **Reuse lesson:** deployment should be a repeatable tool action, but a successful deploy is not a production-security gate.

## Cross-agent clients
- **GrokBot, ChatGPT/Codex, Claude:** used as separate clients against shared application state.
- **Reuse lesson:** test an agent interface across more than one vendor to detect hidden protocol assumptions.
