## Task 107: Add Guardrails to PoC1 and PoC2

Extend the agent pipelines in PoC1 (UserStoryAgent) and PoC2 (RunCoachAgent) with input and output guardrails using the OpenAI Agents SDK.

---

### 🎯 Goal
Ensure both pipelines validate initial user input and final output quality before proceeding or displaying results.

---

### 🧱 Where to Add Guardrails

#### PoC1: UserStoryAgent
- **Input Guardrail (on UXAgent or FunctionalSpecAgent)**
  - Detect vague, non-actionable feature requests
  - Flag anything too generic or unsupported for planning
- **Output Guardrail (on DoRVerifierAgent or WriterAgent)**
  - Ensure story is clear, complete, and matches DoR definition
  - Validate all required sections are present

#### PoC2: RunCoachAgent
- **Input Guardrail (on GoalRaceAgent)**
  - Check if the race goal is valid: race type, time goal, date format
  - Flag unrealistic or ambiguous requests
- **Output Guardrail (on CheckRacePlanAgent)**
  - Validate the final training plan is actionable, specific, and week-by-week
  - Ensure plan aligns with user goal and analysis

---

### 🔧 Implementation Notes
- Use:
  ```python
  from agents import (
      input_guardrail, output_guardrail, GuardrailFunctionOutput,
      InputGuardrailTripwireTriggered, OutputGuardrailTripwireTriggered, Runner
  )
  ```
- Define guardrail functions in `agent/guardrails.py`
- Create small prompt-based guardrail agents to evaluate logic
- Return `tripwire_triggered=True` when validation fails
- Log all trace and tripwire data for debugging

---

### 📂 Files to Update
- `pocs/user_story_agent/agent/guardrails.py`
- `pocs/user_story_agent/agent/{ux_agent.py, user_story_writer.py}`
- `pocs/run_coach_agent/agent/guardrails.py`
- `pocs/run_coach_agent/agent/{goal_agent.py, check_agent.py}`
- `prompts/guardrails/*.yaml`

---

### ✅ Output
- Input issues blocked early with feedback
- Output validated against fitness/clarity/coverage
- Trace includes guardrail triggers and summary

This improves robustness and safety for both PoCs while using only SDK primitives and patterns.