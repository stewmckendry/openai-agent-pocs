## Task 103: Build Newcomer Guide Agent (PoC 3)

Build a guided workflow where a newcomer to Ontario/Canada gets custom onboarding steps by interacting with an AI agent.

---

### 🧠 Context
Simulates a case where a user wants guidance on what to do and access when moving to Canada. Uses web search, classification, and plan generation.

---

### 🎯 Instructions for Codex Agents

**Goal**: Build agents to help user identify needs and return services & plans.

**Flow**:
- `NavigatorAgent` (Orchestrator)
  - `NeedsClassifierAgent`: Classify priorities (e.g. healthcare, work)
  - `GovSearchPlannerAgent`: Generate search terms
  - `GovWebSearchAgent`: Fetch results using WebSearch
  - `ServiceMatcherAgent`: Match to known services
  - `OnboardingPlanAgent`: Generate plan/checklist

**Steps**:
1. Use OpenAI LLM + WebSearch tool
2. Accept goal as user input (via CLI or UI)
3. Use MCP to structure output plan (YAML or JSON)
4. Chain evaluator loop to validate plan quality
5. Enable redo from human feedback
6. Trace and visualize flow

---

### 📂 Files to Create
- `agents/poc_3_newcomer/*.py`
- `tools/match_services.py`, `tools/validate_plan.py`
- `scripts/navigate_newcomer.py`
- `prompts/newcomer_*.yaml`
- `resources/sample_service_list.yaml`

See: https://github.com/openai/openai-agents-python/tree/main/docs

Focus on clarity, flow, and traceability.