## Task 101e: Refactor User Story Agents to Full SDK Compliance

This task ensures that all agents in the user story generation flow follow the OpenAI Agent SDK patterns strictly — for traceability, tooling, schema compliance, and agentic structure.

---

### 🧠 Context
The current agents use custom wrappers and `BaseAgent` patterns that diverge from the OpenAI SDK. This task realigns the implementation with official examples.

---

### 🎯 Objectives
- Replace all custom base agents with `openai_agents.Agent`
- Ensure all callable logic is declared with `@tool`
- Agents must be declared using SDK patterns and support `.run()`
- Refactor LLM calls to use SDK context tools or delegate via `tool`
- Remove all custom `.record()` implementations and use `trace.add_event()`
- Replace CLI/manual flow with agent `.run()` where appropriate
- Optional: validate outputs against DoR schema using MCP

---

### ✅ Refactor Checklist
- [ ] Each agent inherits from `openai_agents.Agent`
- [ ] Each logic step is either a `@tool` or `@traceable`
- [ ] Trace structure uses SDK constructs only
- [ ] Output schemas (e.g. DoR) validated explicitly (e.g. via `mcp.validate()`)
- [ ] Remove `BaseAgent`, manual trace logging, and manual `openai` LLM calls

---

### 📂 Target Files
- `agents/poc_1_delivery/user_story_agents/*.py`
- `tools/*.py`: wrap tools with `@tool`
- `scripts/generate_user_stories.py`: ensure CLI invokes `.run()` and outputs trace correctly
- Optional: add schemas in `resources/` with YAML

Use example pattern:
https://github.com/openai/openai-agents-python/blob/main/examples/financial_research_agent/main.py

Outcome should match OpenAI SDK style and use its native agent lifecycle management.