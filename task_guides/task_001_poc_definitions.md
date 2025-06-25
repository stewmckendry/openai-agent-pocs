## Task 001: PoC Definitions for OpenAI Agent SDK Demo

This file defines three Proof-of-Concepts (PoCs) that will be built using the OpenAI Agents SDK, designed to demonstrate human-AI collaboration in real-world use cases.

---

### ✅ PoC 1: AI Delivery Team (Orchestrated Agents)

**Use Case**: A cross-functional team of AI agents assists a delivery lead in transforming a feature idea into production. Includes review, development, testing, deployment, and documentation.

**Flow**:
- `DeliveryLeadAgent` (Orchestrator)
  - `POPlannerAgent`: Break down feature into stories
  - `POReviewAgent`: Align stories with goals
  - `DoRRefinerAgent`: Refine stories to Definition of Ready
  - `DevAgent`: Prototype implementation
  - `TestAgent`: Write and run tests
  - `DeployAgent`: Simulate deploy process
  - `DocsAgent`: Generate docs or changelog
  - *(Optional)*: `ContextLoaderTool` to ingest existing project files or standards

**Highlights**:
- Chained and orchestrated agents
- Preloaded project context (e.g. Git, Confluence)
- Tracing and visualization
- OpenAI model
- CLI/Minimal UI for user approval, redo

---

### 🏃 PoC 2: AI Run Coach (Goal-Oriented Planning Agent)

**Use Case**: A runner sets a goal (e.g. race date, pace), and the agent plans training using Garmin data and public resources.

**Flow**:
- `RunCoachAgent` (Orchestrator)
  - `GoalPlannerAgent`: Interpret goal (date, pace)
  - `RaceResearchAgent`: Generate search terms, use web search tool
  - `StatsCollectorAgent`: Parse Garmin data (manual upload or API)
  - `RunAnalyzerAgent`: Summarize metrics
  - `PerformanceEvaluatorAgent`: Integrate stats + research
  - `RunPlanAgent`: Output personalized plan
  - `CurrentDateTool`: Calculate days until race

**Highlights**:
- Uses real Garmin data (uploaded or downloaded)
- LLM + tools per sub-agent
- Uses Gemini model
- Visual + trace
- Human provides input, sees reasoning, approves
- CLI or hosted playground UI

---

### 🌍 PoC 3: Newcomer Guide to Canada (Navigational Agent)

**Use Case**: Helps newcomers plan move to Ontario/Canada and match to services.

**Flow**:
- `NavigatorAgent` (Orchestrator)
  - `NeedsClassifierAgent`: Understand key goals (e.g. work, housing)
  - `GovSearchPlannerAgent`: Generate search terms
  - `GovWebSearchAgent`: Use OpenAI WebSearch tool
  - `ServiceMatcherAgent`: Map needs to services
  - `OnboardingPlanAgent`: Produce a personalized checklist

**Highlights**:
- Chained and orchestrated agents
- Uses feedback loop pattern (evaluation + redo)
- Trace + visualize
- Human-initiated, reviewable
- OpenAI model

---

### 🤖 Agent Variants Across PoCs
- Sequential chaining
- Sub-agent orchestration
- Loop w/ evaluator agent
- Tracing and visualization for flow
- Model-agnostic (OpenAI, Gemini)
- CLI support with optional hosted playground
- Emphasis on human-led, AI-enabled interactions

### References
- SDK Docs: https://github.com/openai/openai-agents-python/tree/main/docs
- Examples: https://github.com/openai/openai-agents-python/tree/main/examples
- Tracing: https://github.com/openai/openai-agents-python/blob/main/docs/tracing.md
- Visualization: https://github.com/openai/openai-agents-python/blob/main/docs/visualization.md