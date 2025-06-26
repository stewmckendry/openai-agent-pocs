## Task 104b: Add Tracing, Output Chaining, and Story Writer Agent

Extend the user story agent pipeline with trace visualization, intermediate result printing, and a third agent to generate a structured user story. Follow SDK structure exactly.

---

### 🧪 Goal
Enrich the existing 2-agent flow with:
- Tracing and live output printing
- Chained results across agents
- Final user story generation

---

### ⚙️ What to Build

#### 1. **Tracing + Printer Logging**
- Use:
  ```python
  from agents import trace
  from examples.financial_research_agent.printer import print_trace, print_result
  ```
- Wrap each `Runner.run()` call with `with trace("stage"):`
- Log output with `print_result()`

#### 2. **Run Functional + Technical Agents Separately**
- In `deliverylead.py`, replace sequential logic with individual `Runner.run()` calls
- Use functional output as input to technical agent
- Log and trace each stage separately

#### 3. **Add New Agent: UserStoryWriter**
- File: `agents/user_story_writer.py`
- Tool: `write_user_story(functional: str, technical: str)`
- Prompt: `prompts/user_story_writer.yaml`
- Outputs a markdown or structured user story document

#### 4. **Visualize Graph**
- Add `visualize_workflow()` to `deliverylead.py` to render agent structure
- Call from `main.py` after all agents complete

---

### 📂 Affected Files
- `main.py`
- `deliverylead.py`
- `agents/user_story_writer.py`
- `prompts/user_story_writer.yaml`

---

### 📘 Reference SDK
- Example: `examples/financial_research_agent/manager.py`
- SDK: `agents/trace.py`, `printer.py`, `visualize.py`

---

### ✅ Output
- Functional and technical specs logged separately
- Trace of each agent printed live
- Final story output displayed and optionally saved
- Agent graph rendered for visibility

Do not guess SDK behavior — use examples and ask for clarification if uncertain.