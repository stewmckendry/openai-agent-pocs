## Task 104: Restart User Story Agent PoC (Scoped SDK Implementation)

This task restarts the user story generation pipeline using a clean, SDK-compliant structure modeled directly on the `examples/financial_research_agent` example.

---

### 🎯 Scope
Create the minimal working pipeline for PoC1: generating technical specs from user-submitted feature descriptions via sequential agent handoff.

---

### 📂 Folder Structure
```
pocs/user_story_agent/
├── main.py                  # entry point to run agent flow
├── deliverylead.py          # orchestrator Agent with handoffs
├── agents/
│   ├── functional_agent.py  # turns feature into functionality specs
│   └── technical_agent.py   # turns functional spec into tech spec
├── prompts/
│   ├── functional_prompt.yaml
│   └── technical_prompt.yaml
├── resources/
│   └── tech_architecture.md  # used by technical_agent
├── test/
│   ├── sample_input.txt
│   └── run_test.sh
```

---

### ⚙️ Instructions for Codex Agent
- You MUST use the OpenAI Agents SDK:
  - Reference: `examples/financial_research_agent`
  - Use `agents.Agent`, `function_tool`, `Runner`, `draw_graph`, etc.
- You MUST read SDK layout via `site-packages/agents/` and follow it
- You MUST NOT write custom base agent logic
- If unsure about SDK syntax, STOP and ask the Human Lead
- Add rich header comments to every file

---

### 💼 What to Build
- `main.py`: runs the DeliveryLead agent via `Runner.run()`
- `deliverylead.py`: defines the `DeliveryLead` Agent with handoffs to 2 sub-agents
- `agents/functional_agent.py`: receives user feature, outputs functional spec
- `agents/technical_agent.py`: reads `tech_architecture.md`, outputs tech spec
- `prompts/*.yaml`: one for each sub-agent (structured as `prompt:` key)
- `test/`: provide test input and shell script to run the pipeline

---

### ✅ Output
- Minimal, working agent chain with trace + output
- Clean separation between LLM, tools, and handoffs
- Easy to test and extend

---

This task replaces all previous PoC1 efforts. It is self-contained under `pocs/user_story_agent/` and starts clean.