## Codex Agent Guide: OpenAI Agent PoCs

Welcome to the **Codex Agent workspace** for the OpenAI Agent PoCs supporting the CoachingTheMachine blog series.

---

## 🗂️ Repo Structure (Updated)

| Folder                       | Purpose                                                 |
|------------------------------|---------------------------------------------------------|
| `agents/poc_1_delivery/`     | Agents for Delivery Team PoC                           |
| `agents/poc_2_run_coach/`    | Agents for Run Coach PoC                               |
| `agents/poc_3_newcomer/`     | Agents for Newcomer Guide PoC                          |
| `tools/`                     | Shared code tools across PoCs                          |
| `prompts/`                   | Shared prompt templates (YAML/Jinja)                   |
| `workflows/`                 | Shared orchestrators and chain definitions             |
| `resources/`                 | MCP resources, schemas, validation files               |
| `data/`                      | Sample run data, mock search results, configs          |
| `scripts/`                   | CLI runners, test utilities, deployment setup          |
| `task_guides/`               | Task prompts and reviews                               |

## ✅ Agent Checklists

Each task should include:
- Input/output specs
- Mock input or real data
- Logs + trace validation
- Agent flow visual
- Prompt usage

## 📦 Setup
```bash
pip install -r requirements.txt
```

## 🔗 SDK References
- Docs: https://github.com/openai/openai-agents-python/tree/main/docs
- Examples: https://github.com/openai/openai-agents-python/tree/main/examples
- Tracing: https://github.com/openai/openai-agents-python/blob/main/docs/tracing.md
- Visualization: https://github.com/openai/openai-agents-python/blob/main/docs/visualization.md

## 🤝 Coordination
- Work on `main` unless sandboxing a risky change
- Commit only files tied to a task
- Keep human feedback + agent traceability central

## 🧱 Dev Practices
- Use MCP validation
- Human-AI interaction at each stage
- Enable CLI + minimal hosted UI for experimentation

Let’s build AI that builds *with* us — for good.