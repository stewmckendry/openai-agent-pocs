## Task 101: Build AI Delivery Team Agents (PoC 1)

Create the orchestrated agents to support a software delivery lifecycle, starting from a feature idea to deployable code and documentation.

---

### 🧠 Context
This agent flow simulates a human-led, AI-supported delivery team. Each agent is a specialist and uses either LLMs or tools.

---

### 🎯 Instructions for Codex Agents

**Goal**: Implement all agents and tools needed to:
- Accept a user-submitted feature idea (text)
- Break it into stories
- Review for alignment
- Refine for readiness
- Prototype implementation (mocked)
- Test (unit test tool)
- Simulate deployment
- Document output

**Steps**:
1. Create `DeliveryLeadAgent` as orchestrator using OpenAI Agent SDK
2. Create sub-agents: `POPlannerAgent`, `POReviewAgent`, `DoRRefinerAgent`, `DevAgent`, `TestAgent`, `DeployAgent`, `DocsAgent`
3. Implement at least one tool or LLM chain per agent
4. Enable input and output tracing
5. Use guardrails for story and output schemas
6. Load static context files (e.g. `resources/delivery_standards.md`, `data/project_snapshot.json`)
7. CLI entry point (`scripts/deliver_feature.py`)

**Outputs**:
- One JSON artifact per stage
- Human-readable markdown output
- Traced and visualized workflow

---

### 📂 Files to Create
- `agents/poc_1_delivery/*.py`
- `tools/*.py` as needed
- `workflows/delivery_orchestration.py`
- `scripts/deliver_feature.py`
- `prompts/*.yaml`
- `resources/*.md`
- `data/project_snapshot.json`

Use: https://github.com/openai/openai-agents-python/tree/main/docs

Focus on flow completeness. Don’t over-engineer.