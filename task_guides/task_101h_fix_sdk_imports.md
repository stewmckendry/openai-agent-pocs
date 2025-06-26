## Task 101h: Fix Imports and Naming to Match SDK Structure

Ensure all SDK imports align with the published OpenAI Agents SDK structure and its internal `src/agents` layout.
Codex Agents should not guess or alias SDK components — they must mirror the `openai-agents` structure exactly.

---

### 🎯 Goals
- Fix incorrect import paths across all agents, tools, scripts
- Follow documentation and inspect source at `src/agents/` if unsure
- Eliminate aliases like `from openai_agents import Agent` or `from agents import tool`

---

### 🐞 Known Bugs and Fixes

#### ❌ Bug: Incorrect Agent Import
```python
from openai_agents import Agent  # or from agents import Agent
```
✅ Fix (per SDK):
```python
from agents.agent import Agent
```

#### ❌ Bug: Incorrect Tool Import
```python
from agents.tools import tool
```
✅ Fix (per SDK docs: https://github.com/openai/openai-agents-python/blob/main/docs/tools.md):
```python
from agents import tool
```

#### ❌ Bug: Incorrect traceable Import
```python
from agents import traceable
```
✅ Fix (per SDK docs: https://github.com/openai/openai-agents-python/blob/main/docs/tracing.md):
```python
from agents.tracing import traceable
```

#### ❌ Bug: Incorrect Visualize Import
```python
from agents.visualization import visualize_trace
```
✅ Fix (per SDK docs: https://github.com/openai/openai-agents-python/blob/main/docs/visualization.md):
```python
from agents.visualize import visualize_trace
```

---

### 📂 Scope of Files to Review
- `agents/poc_1_delivery/user_story_agents/*.py`
- `tools/*.py`
- `scripts/*.py`

---

### 🔍 Review Guidance
- If Codex Agent is unsure where a symbol comes from, it should browse SDK source tree `src/agents/`
- Avoid wrapper modules or renaming aliases — match SDK structure literally

---

### ✅ Output
- All imports fixed across repo
- Only SDK-compliant import paths remain
- Output patch report in `task_guides/reports/task_101h_import_fixes_report.md`

---

Let’s keep the repo 100% aligned with SDK so future upgrades, validations, and collaborations are seamless.