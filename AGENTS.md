## Codex Agent Guide: OpenAI Agent PoCs

Welcome to the **Codex Agent workspace** for the OpenAI Agent PoCs supporting the CoachingTheMachine blog series.

---

## 🗂️ Repo Structure (Proposed)

| Folder               | Purpose                                             |
|----------------------|-----------------------------------------------------|
| `agents/`            | All OpenAI Agent SDK implementations                |
| `tools/`             | Code function tools for agents                      |
| `prompts/`           | Prompt YAMLs or Jinja templates                    |
| `workflows/`         | Reusable agent workflows (orchestrators, chains)   |
| `resources/`         | Schemas, config, and MCP metadata                  |
| `data/`              | Sample inputs or mock data for testing             |
| `scripts/`           | Scripted tests, runners or deployment utilities    |
| `task_guides/`       | Prompts and guides for development tasks           |

## 🔁 Naming Conventions

- Tasks: `task_guides/task_<ID>_<desc>.md`
- Workflows: `workflows/<topic>_<step>.py`
- Agents: `agents/<agent_name>.py`
- Tools: `tools/<function_name>.py`

## ✅ Agent Checklists

Each task should include:
- Input/output specs
- Sample inputs and outputs
- Function logic with logs
- Prompt or tool usage
- Tracing verification
- Agent flow visualizations (if applicable)

## ⚙️ Technologies

- **OpenAI Agents SDK**: core framework for agent workflows
- **Model Context Protocol (MCP)**: standardize model inputs/outputs
- **OpenAI/Gemini**: for model-agnostic design
- **Python**: fastapi for tool servers if needed

## 📦 Setup

Install all packages:
```bash
pip install -r requirements.txt
```

Add secrets via `.env`, example provided in `.env-example`

## 🤝 Coordination

Agents should:
- Work on `main` branch unless specified
- Commit only files linked to your task
- Reference `task_guides` for clear requirements
- Use logs + trace processors to aid debugging

---

## 🧱 Development Practices

- Use structured logs and trace metadata
- Modularize and document each tool/agent
- Reuse components across PoCs
- Use MCP resource loading helpers for schema/input validation
- Visualize agent steps where possible

Let’s build AI that builds with us — for good.