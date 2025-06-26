## Task 104c: Global Trace and Full Multi-Agent Story Pipeline

Extend the user story PoC with a global trace and a full pipeline of agents spanning UX, acceptance, estimation, and validation. Follow OpenAI Agent SDK structure.

---

### 🧠 Objective
Build a full agentic pipeline for generating Definition of Ready (DoR)-validated user stories with live tracing and rich agent chaining.

---

### 🛠 What to Build

#### 1. **Global Trace Setup**
- In `main.py` or `DeliveryLead.run()`, create a trace block:
  ```python
  from agents import trace, gen_trace_id
  trace_id = gen_trace_id()
  with trace("user_story_pipeline", trace_id=trace_id):
      # call agents here
  ```
- Optionally print OpenAI trace viewer URL using `print(f"https://platform.openai.com/traces/trace?trace_id={trace_id}")`

#### 2. **New Agents to Add**
- `UXAgent`: input = feature, output = UX spec with personas + journeys
- `AcceptanceCriteriaAgent`: input = functional + technical specs, output = gherkin-style A/Cs
- `ImpactAssessmentAgent`: input = functional + tech specs + resources (`resources/backlog.md`, `as_is_design.md`, `code/`), output = change impact
- `StorypointEstimatorAgent`: input = impact summary, output = Fibonacci story point
- `DoRVerifierAgent`: input = user story draft, output = DoR passed + updated story. Wrap this in a `while not passes:` loop

#### 3. **Update `UserStoryWriterAgent`**
- Inputs: UX spec, functional spec, tech spec, A/Cs, impact, storypoint
- Output: structured user story using markdown template

---

### 📂 Affected Files
- `pocs/user_story_agent/agents/`
- `pocs/user_story_agent/prompts/`
- `pocs/user_story_agent/resources/`: add mock `backlog.md`, `as_is_design.md`
- `pocs/user_story_agent/main.py`, `deliverylead.py`

---

### 📘 References
- `examples/financial_research_agent/manager.py`
- `agents/trace.py`, `agents/gen_trace_id`

---

### ✅ Output
- Agent output and trace for each step
- Global trace linking all agent stages
- Final user story written, DoR-validated, and printed
- Graph generated of full pipeline

Codex MUST NOT guess SDK internals. If uncertain on chaining or trace handling, pause and prompt for clarification.