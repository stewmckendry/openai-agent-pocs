# User Story Agent PoC

This Proof of Concept converts a short feature request into a Definition of Ready compliant user story using the OpenAI Agents SDK. A Delivery Lead agent orchestrates a sequence of specialized sub-agents to produce intermediate specifications and the final story.

## Pipeline

1. **UX Agent** – outlines target personas and user journeys.
2. **Functional Agent** – writes functional requirements based on the feature and UX spec.
3. **Technical Agent** – generates a technical specification using the reference architecture.
4. **Acceptance Agent** – drafts Gherkin-style acceptance criteria.
5. **Impact Agent** – summarizes code and documentation impact.
6. **Estimation Agent** – estimates story points with the Fibonacci scale.
7. **User Story Writer** – combines all specs into a markdown user story.
8. **DoR Verifier** – iteratively checks the story against the Definition of Ready.

Each stage prints its output to the console so you can see the UX, functional, technical, acceptance, impact and estimation results before the final story is displayed.

## Files
- `main.py` – entry point that runs the pipeline
- `deliverylead.py` – orchestrates the agents above
- `agent/` – individual agent modules
- `prompts/` – YAML prompt templates
- `resources/tech_architecture.md` – reference architecture for the technical agent
- `outputs/` – saved user stories and workflow images
- `test/` – sample input and a simple test runner

## Running
Install dependencies and run:

```bash
python -m pocs.user_story_agent.main
```

You can also provide the sample input:

```bash
python -m pocs.user_story_agent.main < pocs/user_story_agent/test/sample_input.txt
```

During execution all intermediate specs and the final user story are printed. The results are saved in `pocs/user_story_agent/outputs/` as a timestamped markdown file and a workflow diagram image.
