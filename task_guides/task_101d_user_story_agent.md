## Task 101d: Refocus Delivery Agent on User Story Generation (PoC 1)

Refactor the delivery team agent from full delivery lifecycle to a more realistic, high-impact slice: generating high-quality, DoR-compliant user stories from a user-provided feature.

---

### 🧠 Context
Generating well-formed, estimated, and accepted user stories ready for development is a known delivery bottleneck. This task builds an agent team that solves this pain point.

---

### 🎯 Instructions for Codex Agents

**Goal**: Implement an agent (`UserStoryLeadAgent`) that orchestrates sub-agents to output DoR-ready user stories from a user-described feature.

---

### 🧩 Sub-Agent Roles
- `UXSpecAgent`: define user experience, journey, and personas
- `FunctionalityAgent`: define required functional behaviour
- `TechSpecAgent`: specify technical architecture or modules
- `AcceptanceCriteriaAgent`: write Gherkin-style acceptance criteria
- `StoryEstimationAgent`: apply story point estimation
- `DoRReviewAgent`: validate the output meets Definition of Ready
- `ImpactAssessmentAgent`: assess impact on existing systems/designs

Optional:
- `TechContextAgent`: understands tech stack (e.g. Salesforce, custom portal) from context file or user prompt
- `IntegrationCheckAgent`: checks for integration points

**User Input**:
- Feature summary (free text)
- Tech stack or platform (optional)
- Integration context (optional)

---

### 🔧 Requirements
- Implement using OpenAI Agents SDK
- Use `traceable`, `Agent`, `@tool` appropriately
- Trace and visualize output (use `draw_graph`)
- Guardrail: output must match DoR schema (use MCP or structured class)
- Generate structured artifacts: YAML/JSON for story output, Markdown for readability
- Add CLI: `scripts/generate_user_stories.py`

---

### 📂 Files to Create/Update
- `agents/poc_1_delivery/user_story_agents/*.py`
- `tools/impact_assess.py`, `tools/estimate_story.py`, etc.
- `resources/dor_schema.yaml`, `resources/tech_context.json`
- `prompts/user_story_*.yaml`
- `scripts/generate_user_stories.py`

---

### 🔍 Output
- Traced and visualized agent run
- Structured user story artifact per feature
- Human CLI interface

This task replaces full-lifecycle orchestration with a single delivery-critical activity.