# Tools

This system is tool-agnostic at its core. Tool names below are source examples, not architectural requirements.

## Codex / local agent workspace
- **Source state:** EXACT
- **Role in source:** interactive agent environment where Riley runs tasks, uses skills and composes workflows.
- **Durable lesson:** the skill lifecycle should not depend on one chat's hidden context.

## YouTube Researcher skill
- **Source state:** EXACT as an example
- **Role:** retrieve/analyze YouTube research inputs.
- **Durable lesson:** external retrieval capability can be encapsulated as a primitive and composed with other skills.

## Remotion skill / best-practices skill
- **Source state:** EXACT as an example
- **Role:** reusable video/visual production procedure.
- **Durable lesson:** domain-specific procedural knowledge can be wrapped into a reusable capability.

## Excalidraw skill
- **Source state:** EXACT as an example
- **Role:** turn ideas/content into visual diagrams/slides.
- **Durable lesson:** skills can transform unstructured thought into structured artifacts.

## Paper / visual board
- **Source state:** EXACT as an example
- **Role:** collect visual references and generate/organize variants.
- **Durable lesson:** visual-context tools can be composed with research skills; human selection remains important.

## Notion / Docs / calendar / email integrations
- **Source state:** EXACT at the integration-pattern level
- **Role:** reduce tab switching and let the agent create/update real records.
- **Durable lesson:** mature workflows should connect to the appropriate system of record/action rather than terminate as disposable chat output.

## Cloud agents / Slack-style interfaces
- **Source state:** EXACT as source discussion, product details subject to commercial bias and rapid change
- **Role:** unattended or collaborative agent execution.
- **Durable lesson:** recurring workflows may need a cloud runtime rather than a local computer.

## Golfkuponger implementation note
Do not copy Riley's exact tool stack by default. Reuse the mechanism and choose the simplest available tool that satisfies the workflow, permissions, reliability and cost requirements.
