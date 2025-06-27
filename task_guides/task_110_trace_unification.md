## Task 110: Unify Agent Traces Under a Single Workflow Trace ID

Refactor PoC agent pipelines to ensure all agent steps are grouped under a single `trace_id` so they appear as one trace in the OpenAI trace viewer.

---

### 🧠 Goal
Consolidate all SDK traces for a PoC into one workflow to improve observability, coherence, and debugging.

---

### 🔧 What to Do

#### 1. **Generate `trace_id` Once at Top Level**
- In `main.py` for each PoC, add:
  ```python
  from agents import gen_trace_id, trace
  trace_id = gen_trace_id()
  with trace("<workflow_name>", trace_id=trace_id):
      await pipeline.run(..., trace_id=trace_id)
  ```

#### 2. **Propagate `trace_id` to All Agents**
- Update each pipeline manager (e.g. `DeliveryLead`, `RunCoachAgent`) to accept `trace_id`
- Pass it into every `Runner.run(agent, input, trace_id=trace_id)` call

#### 3. **Remove or Reuse Inner Traces**
- If sub-agents or tools use `trace(...)`, wrap them like this:
  ```python
  with trace("step_name", trace_id=trace_id):
      ...
  ```
  - Do NOT call `gen_trace_id()` again inside sub-agents

---

### 📂 Files to Update
- `main.py` in each PoC (`pocs/user_story_agent/`, `pocs/run_coach_agent/`, etc.)
- All pipeline orchestrator files (e.g. `runcoach.py`, `tripmanager.py`, `deliverylead.py`)
- Optional: Any agents using local trace spans

---

### ✅ Output
- All agents and sub-agents in a single trace group per run
- Viewer shows nested tool calls and agent chains coherently
- No trace ID collisions or duplications

This makes it much easier to debug agent runs, understand performance, and demo workflows cleanly.