## Task 101b: Refined Build of AI Delivery Team Agents (PoC 1)

Refactor and expand Task 101 to explicitly require use of the OpenAI Agents SDK and its core capabilities. This task replaces Task 101.

---

### 🧠 Context
The goal is to showcase an autonomous, traceable, and human-interactive agent delivery team that follows OpenAI Agent SDK standards. Output should not be mocked — each step should execute and produce traceable artifacts.

---

### 🎯 Updated Instructions for Codex Agents

**Objectives**:
- Implement `DeliveryLeadAgent` using `openai-agents-python`
- Create all supporting sub-agents
- Use the Agents SDK features as follows:

**🔧 REQUIRED FEATURES TO DEMONSTRATE**
- ✅ Agents + sub-agents (orchestrator model)
- ✅ User input at the start (feature idea via CLI prompt)
- ✅ Tracing using `@traceable` and `Trace` constructs
- ✅ Output guardrails and schemas
- ✅ Visualization support (`openai-agents-python` visual extension)
- ✅ LLM calls (story generation, summarization, test logic, etc.)
- ✅ At least one use of `OpenAITool` like `WebSearch`
- ✅ One custom tool (e.g., `validate_DoR`)
- ✅ MCP schema (optional: wrap one agent I/O)

**Flow**:
1. User inputs a feature via CLI
2. `DeliveryLeadAgent` triggers sub-agents:
   - `POPlannerAgent`: creates stories from LLM
   - `POReviewAgent`: uses WebSearch + rules to validate
   - `DoRRefinerAgent`: applies tool to refine readiness
   - `DevAgent`, `TestAgent`, `DeployAgent`, `DocsAgent`: each with traceable output
   - `EvaluatorAgent`: validates story flow and raises flags
3. CLI runner prompts user at key decision points (e.g. approve/refactor stories)
4. All traceable steps visualized via SDK tools

---

### 📂 Files to Create
Same as Task 101, but also:
- Use `agents/poc_1_delivery/` only for agent SDK-compliant code
- Add `visualization/` output to capture graph views
- Ensure `scripts/deliver_feature.py` runs from CLI and logs trace ID

---

### ❌ DO NOT:
- Return placeholder JSONs
- Stub out LLM calls or tools
- Skip SDK decorators or tracing support

---

Use: https://github.com/openai/openai-agents-python/tree/main/docs

Outcome should be runnable, testable, and aligned with SDK intent.