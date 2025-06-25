## Task 001: PoC Definitions for OpenAI Agent SDK Demo

Defines 3 PoCs for showcasing OpenAI Agent SDK capabilities in support of the CoachingTheMachine blog.

---

### ✅ PoC 1: AI Delivery Team (Orchestrated Agents)

**Use Case**: Feature idea → user story → ready tickets → dev → test → deploy → document.

**Flow**:
- `DeliveryLeadAgent` (Orchestrator)
  - `POPlannerAgent`: Craft user stories from idea
  - `POReviewAgent`: Check alignment with goals
  - `DoRRefinerAgent`: Make stories ready
  - `DevAgent`: Write initial implementation
  - `TestAgent`: Write and run tests
  - `DeployAgent`: Simulate deploy
  - `DocsAgent`: Generate feature docs

**Highlights**:
- Orchestration and chaining
- Output guardrails for stories, tickets
- Trace + visualization
- Uses OpenAI

---

### 🏃 PoC 2: AI Run Coach (Goal-Driven Agent Workflow)

**Use Case**: Plan for a goal race (pace/date), analyze Garmin stats, recommend plan.

**Flow**:
- `RunCoachAgent` (Orchestrator)
  - `GoalPlannerAgent`: Take goal race + date/pace
  - `RaceResearchAgent`: Search strategy for race type
  - `StatsCollectorAgent`: Parse Garmin or mock run data
  - `RunAnalyzerAgent`: Summarize run stats + patterns
  - `PerformanceEvaluatorAgent`: Integrate all data for insight
  - `RunPlanAgent`: Suggest weekly running plan

**Features**:
- Sub-agents for tool steps
- Uses current date tool
- LLM+code tools
- Uses Gemini
- Tracing + visual

---

### 🌍 PoC 3: Newcomer Guide to Canada (AI Navigator Agent)

**Use Case**: Someone planning to move to Ontario/Canada gets tailored info.

**Flow**:
- `NavigatorAgent` (Orchestrator)
  - `NeedsClassifierAgent`: Classify intents (e.g., housing, healthcare)
  - `GovSearchAgent`: Fetch info from preloaded datasets or simulate web fetch
  - `ServiceMatcherAgent`: Match to provincial/federal resources
  - `OnboardingPlanAgent`: Return custom checklist/plan

**Highlights**:
- MCP output structure
- Input validation guardrails
- Uses OpenAI
- Feedback loop variant
- Visual + traceable

---

### 🧠 Variants Across PoCs
- **Sequential chaining** (PoC 1)
- **Orchestrator with sub-agents** (PoCs 2 & 3)
- **Evaluator-feedback loop** (PoC 3 variant)
- **Model variation**: OpenAI (1, 3), Gemini (2)
- **Trace & visualize**: All PoCs using OpenAI Agent SDK tracing and visualization tools

### References
- Agent SDK docs: https://github.com/openai/openai-agents-python/tree/main/docs
- Agent SDK examples: https://github.com/openai/openai-agents-python/tree/main/examples
- Visualization: https://github.com/openai/openai-agents-python/blob/main/docs/visualization.md
- Tracing: https://github.com/openai/openai-agents-python/blob/main/docs/tracing.md