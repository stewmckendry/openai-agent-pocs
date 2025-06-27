# Trip Planner Agent PoC

This proof of concept assembles a short travel itinerary from a free form trip request. The agent team researches points of interest and compiles a day‑by‑day plan.

## Target users
- Travelers looking for quick suggestions on what to see and do
- Anyone wanting a structured plan from minimal input

## Benefits
- Automatically searches the web for relevant attractions
- Generates a concise itinerary including transportation and lodging tips
- Rejects vague requests and checks the final plan for quality and safety

## Pipeline overview
1. **Topic Agent** – extracts 3–5 research topics from the trip goal
2. **Research Agent** – searches the web for each topic and summarizes results
3. **Planner Agent** – writes the itinerary and passes it through output guardrails

Progress is printed to the console so you can view topics, research summaries and the final itinerary.

## Inputs and outputs
- **Input:** a text description of your travel goals
- **Output:** a markdown itinerary printed to the console and saved under `outputs/` along with a workflow image


## Future enhancements
- Add budget estimates and restaurant recommendations
- Integrate map links and calendar exports
- Support alternate planning modes like backpacking or luxury travel

## Agents SDK Features

| SDK Feature | Benefit to PoC |
|-------------|----------------|
| `Agent` and `handoffs` | Chain topic, research and planner agents |
| `Runner` | Executes each agent in sequence |
| `WebSearchTool` | Gathers live results for each research topic |
| `input_guardrail` & `output_guardrail` | Validates trip requests and itinerary quality |
| `function_tool` | Provides helper functions such as getting the current date |
| `output_type` (Pydantic) | Returns structured topics, research and plan |
| `trace` | Records a trace for later review |
| `visualization` | Generates a workflow diagram |

## Running
Install dependencies then run:

```bash
python -m pocs.trip_planner_agent.main
```

To try the sample input:

```bash
python -m pocs.trip_planner_agent.main < pocs/trip_planner_agent/test/sample_input.txt
```

The generated plan and diagram appear in `pocs/trip_planner_agent/outputs/`.
