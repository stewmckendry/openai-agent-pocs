# User Story Agent PoC

This proof of concept turns a short feature request into a Definition of Ready compliant user story. A Delivery Lead agent coordinates several specialized agents to gather specifications and write the final story.

## Target users
- Product owners or delivery leads who need consistent user stories
- Developers exploring automated requirements generation

## Benefits
- Quickly expands a one‑line feature request into UX, functional and technical specs
- Provides acceptance criteria and impact analysis
- Iteratively checks that the resulting story meets your Definition of Ready

## Pipeline overview
1. **UX Agent** – outlines target personas and user journeys
2. **Functional Agent** – writes functional requirements using the UX spec
3. **Technical Agent** – generates a technical design using the reference architecture
4. **Acceptance Agent** – drafts Gherkin‑style acceptance criteria
5. **Impact Agent** – summarizes code and documentation impact
6. **Estimation Agent** – estimates story points with the Fibonacci scale
7. **User Story Writer** – combines all specs into a markdown user story
8. **DoR Verifier** – revises the story until it passes the Definition of Ready

Progress for each stage is printed to the console so you can review the intermediate specs.

## Inputs and outputs
- **Input:** a brief feature description and the technical architecture file in `resources/`
- **Output:** the final user story printed to the console and saved under `outputs/` with a workflow image and all intermediate specs

## Future enhancements
- Link directly to issue trackers for story creation
- Add a persona repository for richer UX guidance
- Provide optional code scaffolding based on the technical spec

## Running
Install dependencies and run:

```bash
python -m pocs.user_story_agent.main
```

Try the sample feature description with:

```bash
python -m pocs.user_story_agent.main < pocs/user_story_agent/test/sample_input.txt
```

The generated story and diagram are saved in `pocs/user_story_agent/outputs/`.
