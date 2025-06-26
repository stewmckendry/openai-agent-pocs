## OpenAI Agent PoCs

This repository accompanies the CoachingTheMachine blog series on how humans and AI can co-create solutions for good. It showcases Proof-of-Concept (PoC) implementations using the OpenAI Agents SDK and other frameworks for autonomous, traceable, model-agnostic agent workflows.

### Blog Reference
https://coachingthemachine.substack.com/

### PoC Themes
- AI delivery team agents for software feature lifecycles
- Personal run coach agents integrating Garmin data
- Public sector and health navigation assistants

### Key Goals
- Showcase the OpenAI Agent SDK's capabilities
- Use model-agnostic agent design (OpenAI, Gemini, etc.)
- Demonstrate workflows with guardrails, tool use, tracing, visualization
- Encourage collaboration and real-world application of agentic systems

### Running PoC 1
Execute `scripts/deliver_feature.py` to run the legacy delivery workflow.
Use `scripts/generate_user_stories.py` to generate DoR-compliant user stories for a feature.

#### Testing the CLI
```bash
python scripts/generate_user_stories.py "As a user, I want to upload a CSV of customer contacts to the CRM"
open project/outputs/stories.json
open project/outputs/trace_graph.html
```
Ensure a `.env` file exists with `OPENAI_API_KEY` (see `.env-example`).
