## Task 002: Mapping SDK Features to PoCs

This document confirms which features of the OpenAI Agents SDK are demonstrated across the three PoCs.

Reference: https://github.com/openai/openai-agents-python/tree/main/docs

---

### ✅ Feature Coverage by PoC

| Feature               | PoC 1: Delivery Team         | PoC 2: Run Coach           | PoC 3: Newcomer Guide       |
|-----------------------|------------------------------|-----------------------------|-----------------------------|
| Agents               | ✅ Yes (8+ agents)           | ✅ Yes (6 agents)          | ✅ Yes (5 agents)          |
| Multi-Agents         | ✅ Orchestrated + Sequential | ✅ Orchestrated             | ✅ Orchestrated + Evaluator |
| Handoffs             | ✅ Between agents            | ✅ Planner → Analyzer      | ✅ Planner → Search → Match |
| Input Types/Schemas  | ✅ Feature idea text         | ✅ File + goal string       | ✅ Goal/intent text         |
| Output Types/Schemas | ✅ JSON + markdown           | ✅ JSON plan                | ✅ YAML/JSON checklist      |
| Tools                | ✅ Custom tools + OpenAI     | ✅ Garmin parsers, Gemini   | ✅ WebSearch + custom       |
| OpenAI Tools         | ✅ WebSearch (optional)      | ✅ WebSearch                | ✅ WebSearch                |
| Custom Tools         | ✅ Dev/test/deploy/doc utils | ✅ parse_garmin, stats      | ✅ plan validator, matcher  |
| MCP Resources        | ✅ Reused input schemas      | ✅ Model context resources  | ✅ Service definitions      |
| Guardrails           | ✅ Output schema validation  | ✅ Garmin input format      | ✅ Plan structure schema    |
| Results              | ✅ CLI + logs                | ✅ JSON/CLI + trace         | ✅ Checklist + trace        |
| Tracing              | ✅ Full SDK tracing          | ✅ Full SDK tracing         | ✅ Full SDK tracing         |
| Visualization        | ✅ SDK visual enabled        | ✅ Visual flow output       | ✅ Agent path view          |

---

### 🔍 Gaps + Proposals
- **Feedback loops** (evaluator agent) — implemented only in PoC 3; consider adding PO feedback loop in PoC 1
- **MCP validation layers** — solid in PoC 3; light touch in PoC 1/2, can be added to validate agent-to-agent messages
- **WebSearch in PoC 1** — could use OpenAI WebSearch to pull coding practices

---

### ✅ Recommendations
- Enhance `POReviewAgent` in PoC 1 to optionally search for similar stories or standards via WebSearch
- Use MCP schemas to validate intermediate agent outputs (e.g. DevAgent's code output)
- Add `ValidatorAgent` in PoC 2 to refine training plans based on feedback loop

---

### 📂 Location
This mapping is committed to `task_guides/task_002_sdk_features_mapping.md`