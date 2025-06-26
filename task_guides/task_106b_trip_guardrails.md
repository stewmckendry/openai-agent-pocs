## Task 106b: Add Guardrails to TripPlannerAgent (Input + Output Validation)

Integrate built-in OpenAI Agents SDK guardrails into PoC3 to catch vague or problematic input and low-quality itinerary output.

---

### 🎯 Goal
Improve the safety and quality of trip planning by validating:
- Input clarity and feasibility (via `TopicAgent`)
- Output realism and specificity (via `PlannerAgent`)

---

### 🛠 What to Build

#### 1. **Input Guardrail: `vague_trip_guardrail`**
- Detects trip inputs that are:
  - Too vague (“somewhere fun”)
  - Unsafe/inappropriate (e.g. “escape society”)
  - Not actionable
- Define guardrail agent:
  ```python
  Agent(name="Trip Input Check", instructions="Flag if trip request is vague, unsafe, or unsupported.")
  ```
- Hook into `TopicAgent`:
  ```python
  input_guardrails=[vague_trip_guardrail]
  ```

#### 2. **Output Guardrail: `trip_quality_guardrail`**
- Ensures final plan includes:
  - Destinations, activities, transportation, accommodations
  - Realism, safety, specificity
- Attach to `PlannerAgent`:
  ```python
  output_guardrails=[trip_quality_guardrail]
  ```
- Output schema:
  ```python
  class TripOutput(BaseModel):
      response: str
  ```

#### 3. **Guardrail Functions**
Example pattern:
```python
@input_guardrail
async def vague_trip_guardrail(ctx, agent, input):
    result = await Runner.run(guardrail_agent, input)
    return GuardrailFunctionOutput(...)

@output_guardrail
async def trip_quality_guardrail(ctx, agent, output):
    result = await Runner.run(guardrail_agent, output.response)
    return GuardrailFunctionOutput(...)
```

---

### 📂 Files to Update
- `agent/topic_agent.py` → input guardrail
- `agent/planner_agent.py` → output guardrail
- `agent/guardrails.py` → guardrail functions and helper agents
- `prompts/guardrail_input_check.yaml`, `guardrail_output_check.yaml`

---

### ✅ Output
- Input issues blocked early
- Output validated before delivery
- Trace logs guardrail results and tripwire triggers

This strengthens PoC3’s safety, usability, and LLM efficiency.