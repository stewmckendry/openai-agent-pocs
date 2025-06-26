# User Story Agent PoC

This Proof of Concept demonstrates a minimal sequential workflow built with the OpenAI Agents SDK. A feature description is transformed into a functional specification and then into a technical specification using two dedicated sub-agents.

## Files
- `main.py` – entry point that runs the pipeline
- `deliverylead.py` – orchestrator agent with handoffs
- `agents/functional_agent.py` – converts a feature into a functional spec
- `agents/technical_agent.py` – converts the functional spec into a technical spec
- `prompts/` – YAML prompt templates
- `resources/tech_architecture.md` – reference architecture for the technical agent
- `test/` – sample input and a simple test runner

## Running
Install dependencies and run:

```bash
python -m pocs.user_story_agent.main
```

Follow the prompts or pipe a file with the feature description as input.
