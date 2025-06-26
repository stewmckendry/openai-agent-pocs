## Task 106: Create Trip Planner Agent PoC (PoC3)

Create an agent pipeline that helps users plan trips using web search and itinerary generation, grounded in current date and user interests.

---

### 🧠 Goal
Turn high-level user travel goals into detailed, researched travel itineraries with traceable agentic steps.

---

### 🧱 Pipeline Flow
```
main.py → TripPlanningManager → [TopicAgent → ResearchAgent → PlannerAgent]
```

1. **User Input**: CLI entry describing destination and travel goals
2. **TopicAgent**: Generates research queries across all areas of trip planning
   - Includes a tool `get_current_date()` to ground references like “in the fall”
3. **ResearchAgent**: Uses `WebSearchTool` (from SDK) to run searches per topic
   ```python
   from agents import WebSearchTool
   ```
4. **PlannerAgent**: Synthesizes search results + topics to generate:
   - Summary of planning factors (e.g., vaccines, weather, events)
   - Day-by-day itinerary

---

### 📂 File Structure
```
pocs/trip_planner_agent/
├── main.py                  # CLI entry
├── tripmanager.py           # Orchestrator agent
├── agent/
│   ├── topic_agent.py       # Generates search topics
│   ├── research_agent.py    # Web search executor
│   └── planner_agent.py     # Final itinerary builder
├── prompts/
│   ├── topic_prompt.yaml
│   ├── research_prompt.yaml
│   └── plan_prompt.yaml
├── test/
│   ├── sample_input.txt
│   └── run_test.sh
```

---

### ⚙️ Instructions for Codex Agent
- Use OpenAI Agent SDK only: `Agent`, `Runner`, `trace`, `function_tool`, `WebSearchTool`
- Follow examples from:
  - `pocs/user_story_agent/`
  - `pocs/run_coach_agent/`
  - `examples/research_bot` (for search agents)
- NEVER use custom base agent logic
- MUST pause and prompt if syntax or SDK usage is unclear
- All code must include rich header comments

---

### ✅ Output
- Travel planning output in markdown
- Includes search topics, research responses, final plan
- Full trace and graph available for each run
- Print results to console using `printer.py`

This PoC will demonstrate agentic planning from open-ended queries using real-time research, personalized itinerary construction, and traceable decision paths.