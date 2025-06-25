## Task 102: Build AI Run Coach Agent (PoC 2)

Construct an agent that helps a user plan for a goal race using their Garmin data and online insights.

---

### 🧠 Context
The agent flow reflects how a personal coach might synthesize goal, public research, and user stats into a training plan.

---

### 🎯 Instructions for Codex Agents

**Goal**: Implement a run coaching agent using:
- Uploaded Garmin `.fit` or JSON run data
- User-defined goal (race, date, pace)
- Web search via OpenAI tool

**Flow**:
- `RunCoachAgent` (Orchestrator)
  - `GoalPlannerAgent`: Parse user goal
  - `RaceResearchAgent`: Generate search queries, use WebSearch
  - `StatsCollectorAgent`: Parse run file
  - `RunAnalyzerAgent`: Summarize pace, cadence, etc.
  - `PerformanceEvaluatorAgent`: Integrate all inputs
  - `RunPlanAgent`: Suggest weekly plan

**Steps**:
1. Implement sub-agents using SDK
2. Use Gemini as LLM provider
3. Support CLI file input (`scripts/plan_run.py`)
4. Enable tracing and visualize agent flow
5. Log input/output and enable retry flow
6. Use real Garmin data sample or mock if needed

---

### 📂 Files to Create
- `agents/poc_2_run_coach/*.py`
- `tools/parse_garmin.py`, `tools/analyze_stats.py`
- `scripts/plan_run.py`
- `prompts/runcoach_*.yaml`
- `data/garmin_sample.json`

Use: https://github.com/openai/openai-agents-python/tree/main/examples

Focus on utility + clarity. Assume minimal UI or CLI.