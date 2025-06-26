## Task 105b: Race Goal Enhancements for Run Coach Agent

Improve the GoalRaceAgent’s accuracy by incorporating current date context and enhance output formatting for transparency and review.

---

### 🧠 Objectives
1. Use real-time date in race goal calculation
2. Include intermediate outputs in the Markdown file

---

### ⚙️ What to Build

#### 1. **Current Date Tool in GoalRaceAgent**
- Add a tool: `@function_tool def get_current_date() -> str`
- Use `datetime.datetime.now().date().isoformat()` to return today’s date
- Inject the result into the prompt context to anchor any month-based inputs (e.g., "October")
- Example YAML addition:
  ```yaml
  current_date: 2025-06-26
  user_input: "I want to run a marathon in October"
  ```

#### 2. **Update Output Display**
- In `runcoach.py` and `main.py`, capture outputs from:
  - `goal_result`
  - `parsed_runs`
  - `analysis_result`
  - `training_plan`
- Format final Markdown with:
  ```markdown
  # Your Race Input
  [User Input Here]

  # Race Goal
  [Parsed Goal Output]

  # Current Run Stats
  [Parsed CSV Summary]

  # Run Analysis
  [Analysis Agent Output]

  # Training Plan
  [Final Plan Markdown]
  ```

#### 3. **Where to Apply Changes**
- Update `pocs/run_coach_agent/agent/goal_agent.py`
- Update `pocs/run_coach_agent/runcoach.py`
- Update `pocs/run_coach_agent/main.py`

---

### 📘 Reference Example
- See global trace and printer strategy in `examples/financial_research_agent/manager.py`
- Follow SDK conventions (`function_tool`, `trace`, `draw_graph`, `Runner`)

---

### ✅ Output
- Race goals now aligned with present-day timeline
- Output Markdown includes intermediate agent steps
- Better debugging + visibility for the user

This improves realism, auditability, and output structure for the race coaching experience.