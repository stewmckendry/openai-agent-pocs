# Run Coach Agent PoC

This proof of concept creates a personalized running plan using a small team of agents. It reads your recent Garmin `Activities.csv` and a free form race goal, then outputs a week‑by‑week training schedule.

## Target users
- Recreational runners preparing for an upcoming race
- Anyone wanting a quick assessment of their current running stats

## Benefits
- Automatically analyzes your latest runs
- Produces an achievable plan tailored to your race date and pace goal
- Saves the plan and a workflow diagram for later review

## Pipeline overview
1. **Goal Agent** – parses the race description into distance, date and pace targets
2. **Collect Agent** – loads recent runs from `Activities.csv`
3. **Analyze Agent** – finds training strengths and gaps
4. **Plan Agent** – writes a week‑by‑week schedule
5. **Check Agent** – validates the plan and revises if needed

Each stage prints progress to the console so you can see the goal, collected data, analysis and final plan.

## Inputs and outputs
- **Input:** a text description of your race goal and the Garmin CSV located in `resources/Activities.csv`
- **Output:** the final training plan in the console and a markdown file under `outputs/` along with a workflow image

## Future enhancements
- Support other fitness data sources such as Strava
- Add injury risk detection and calendar export
- Offer multiple plan strategies based on user experience

## Running
Install dependencies then execute:

```bash
python -m pocs.run_coach_agent.main
```

You can try the sample goal with:

```bash
python -m pocs.run_coach_agent.main < pocs/run_coach_agent/test/sample_goal.txt
```

Your plan and diagram will be saved in `pocs/run_coach_agent/outputs/`.
