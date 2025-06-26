## Task 105: Create Run Coach Agent PoC (PoC2)

Set up a new agentic pipeline under `pocs/run_coach_agent/` that guides a runner toward their race goal based on user goals and personal run stats.

---

### 🧠 Goal
Use the OpenAI Agent SDK to build a chain of agents that take a goal race and past running data to produce a tactical, week-by-week training plan.

---

### 🧱 Pipeline Flow
```
main.py → RunCoachAgent → [GoalRaceAgent → CollectRunStatsAgent → AnalyzeRunStatsAgent → PlanRaceAgent → CheckRacePlanAgent]
```

1. **User Input**: CLI input for feature (race description)
2. **GoalRaceAgent**: Turn user input into structured goal (race type, date, distance, time goal, weeks to train)
3. **CollectRunStatsAgent**: Load user's `Activities.csv` from `resources/`, parse and validate recent runs
4. **AnalyzeRunStatsAgent**: Analyze patterns, strengths, and gaps vs goal
5. **PlanRaceAgent**: Draft multi-week race prep plan based on stats + goal
6. **CheckRacePlanAgent**: Reviews plan for realism, specificity, clarity; may revise
7. **Printer**: Console + Markdown output of final plan
8. **Trace**: Log global trace like PoC1

---

### 📂 File Structure
```
pocs/run_coach_agent/
├── main.py                      # CLI entry
├── runcoach.py                  # Orchestrator agent logic
├── agent/
│   ├── goal_agent.py
│   ├── collect_agent.py
│   ├── analyze_agent.py
│   ├── plan_agent.py
│   └── check_agent.py
├── prompts/
│   ├── goal_prompt.yaml
│   ├── collect_prompt.yaml
│   ├── analyze_prompt.yaml
│   ├── plan_prompt.yaml
│   └── check_prompt.yaml
├── resources/Activities.csv     # User run history (sample uploaded)
├── test/
│   ├── run_test.sh
│   └── sample_goal.txt
```

---

### ⚙️ Instructions for Codex Agent
- Use the SDK (from `agents`) ONLY:
  - `Agent`, `function_tool`, `Runner`, `trace`, `draw_graph`
- Follow SDK layout used in PoC1 and `examples/financial_research_agent`
- Use the provided CSV as test data (resources/Activities.csv)
- Pause and ask if unsure about SDK syntax — guessing is not allowed
- All files must have rich header comment

---

### ✅ Output
- Working pipeline that logs and prints tactical run plan
- Graph and trace available after execution
- Ready for extension into UI or hosted service