## Task 101g: Refactor User Story Agents for True Agentic Flow via Handoffs

Refactor PoC 1 agents to use SDK-style `handoffs` between agents and eliminate hardcoded tool calls, aligning with OpenAI Agent SDK agent orchestration best practices.

---

### 🎯 Goal
Build a fully agentic user story generation flow where agents communicate via handoffs, tools are delegated automatically, and the runner orchestrates the entire execution graph.

---

### 🧱 Required Refactor

1. **Remove manual `.run()` chaining in UserStoryLeadAgent**
2. **Define tools explicitly with `@tool` and assign to each agent**
3. **Declare `handoffs=[(tool_name, agent)]` in each agent constructor**
4. **Ensure `Runner.run({"feature": "..."})` can flow from lead agent through all dependencies**
5. **Eliminate custom logic in `UserStoryLeadAgent.run()`**
6. **Trace output should reflect agent-to-agent handoff paths**

---

### 🗂️ Files to Update
- `agents/poc_1_delivery/user_story_agents/user_story_lead_agent.py`
- All sub-agents: remove `.run()` wrappers, declare `@tool`, set `handoffs`
- `scripts/generate_user_stories.py`: no change if already using `Runner`

---

### 🧠 Reference Example
Use this SDK example now included in the repo:
```
examples/financial_research_agent/
```
Key references:
- `planner_agent.py`, `search_agent.py`, `manager.py`
- Agent creation and `handoffs` wiring
- No `.run()` in orchestrator — only `Runner.run()`

---

### ✅ Output
- Graph-driven trace from feature → context → ux → tech → est → review → done
- `runner.get_result()` returns structured JSON
- `draw_graph(trace)` visualizes agentic workflow

This structure will enable reuse, visibility, and downstream extensibility (e.g., evaluator loops, retries, etc.).