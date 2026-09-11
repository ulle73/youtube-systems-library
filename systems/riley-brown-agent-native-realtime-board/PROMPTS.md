# Prompt Patterns

## Five-part build brief
Use this as a structure, not as a verbatim Riley prompt:

1. **Platform** - state the target runtime/product surface.
2. **Reference app** - name a familiar product or interaction model when it meaningfully reduces ambiguity.
3. **User flow** - describe the important actions in order, including human/agent identity and attribution.
4. **Design direction** - give a concise visual/product direction; leave cheap details iterative.
5. **Database/state choice** - specify persistence/realtime requirements when they materially constrain architecture.

## First-pass QA prompt pattern
After the initial build, review one complete batch across:
`Function -> Layout -> Mobile -> Data/realtime -> Test edge cases -> Secure`

Ask the coding agent to fix the set coherently and then rerun checks, rather than assuming first-pass generation is finished.

## Cross-agent interoperability test
Give a second agent the same application interface and ask it to:
- read current state first;
- create one uniquely identifiable test record;
- edit/comment using difficult punctuation or realistic data;
- report the resulting state;
- avoid duplicate work.

## Production adaptation
Never put long-lived secrets inside a portable prompt/skill. Use scoped runtime credentials and make the skill describe how authentication is obtained, not the secret itself.
