## Task 109: Enable LLM Model Selection via LiteLLM Proxy

Enable any PoC to support dynamic selection of model provider (e.g. OpenAI, Gemini, Claude) using LiteLLM-compatible interface.

---

### 🧠 Goal
Add CLI option to configure the model + API key and pass it to the Agent using `LitellmModel`, as shown in:
```
examples/model_provider/litellm_provider.py
```

---

### 🧱 Use Case
- Let user choose between `openai/gpt-4o`, `gemini/gemini-1.5-flash`, or other LiteLLM-compatible models
- Load model+key from CLI args or fallback to `.env`

---

### 🧩 What to Build

#### 1. **Update CLI in `main.py` (any PoC)**
- Add:
```python
parser.add_argument("--model", type=str, help="Model to use (e.g. openai/gpt-4o)")
parser.add_argument("--api-key", type=str, help="API key for the model")
```
- If not passed, fallback to `os.environ["MODEL"]` and `os.environ["MODEL_API_KEY"]`

#### 2. **Inject into agent model**
- Wherever an agent is constructed (e.g. `DeliveryLeadAgent`, `RunCoachAgent`), insert:
```python
from agents.extensions.models.litellm_model import LitellmModel
...
model = LitellmModel(model=model_name, api_key=api_key)
agent = Agent(..., model=model)
```
- Pass `model` to sub-agents if needed

---

### 🧪 Setup
- Add `.env-example`:
```env
MODEL=openai/gpt-4o
MODEL_API_KEY=sk-xxx
```
- You must install `litellm` and use a valid provider model string (see https://docs.litellm.ai/docs/providers)

---

### ✅ Output
- Run like:
```bash
poetry run python -m pocs/user_story_agent/main.py --model openai/gpt-4o --api-key $OPENAI_API_KEY
```
- Agent runs using that provider
- Output and trace show model used

---

This unlocks multi-provider experimentation across all PoCs using SDK-standard tooling.