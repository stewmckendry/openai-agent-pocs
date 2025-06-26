## Task 101e: Refactor User Story Agents to Full SDK Compliance

This task ensures that all agents in the user story generation flow follow the OpenAI Agent SDK patterns strictly — for traceability, tooling, schema compliance, and agentic structure.

---

### 🧠 Context
The current agents use custom wrappers and `BaseAgent` patterns that diverge from the OpenAI SDK. This task realigns the implementation with official examples.

---

### 🎯 Updated Objectives
- Replace all custom base agents with `openai_agents.Agent`
- Define logic as tools using `@tool` decorator
- Build the full agent flow using `Runner` and `Runner.run()` for orchestration
- Remove manual `Trace()` logic and rely on SDK trace generation
- Validate outputs using SDK result schema or custom `pydantic` models
- CLI script should use `Runner.run()` and visualize trace with `draw_graph`

---

### ✅ Refactor Checklist
- [ ] All agents inherit from `openai_agents.Agent` using `name`, `instructions`, `tools`, and `handoffs`
- [ ] Each logical step is declared using `@tool`
- [ ] Remove custom `BaseAgent`, `.record()`, or `.merge()` patterns
- [ ] CLI entry script uses `Runner.run()` with `inputs` dictionary
- [ ] Trace is visualized using `draw_graph(trace)` and/or `visualize_trace`
- [ ] Output is retrieved using `runner.get_result()` and saved
- [ ] Optional: use `mcp.validate()` or `pydantic` schemas to verify story output structure

---

### 📂 Files to Update
- `agents/poc_1_delivery/user_story_agents/*.py`
- `tools/*.py` — refactor as `@tool`
- `scripts/generate_user_stories.py` — run agent via `Runner`
- `resources/` — define schemas (optional)

---

### 📘 Reference Examples
- [Runner Docs](https://github.com/openai/openai-agents-python/blob/main/docs/running_agents.md)
- [Results Docs](https://github.com/openai/openai-agents-python/blob/main/docs/results.md)
- [Financial Research Example](https://github.com/openai/openai-agents-python/blob/main/examples/financial_research_agent/manager.py)

This task will align the implementation with best practices for observability, composability, and traceable AI execution.