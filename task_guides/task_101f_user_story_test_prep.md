## Task 101f: Prepare Testing and Documentation for User Story Agents (PoC 1)

Enhance code quality, reproducibility, and usability by documenting all components, setting up test instructions, and ensuring ready-to-run outputs.

---

### 🧠 Context
Once Task 101e completes the SDK refactor, this task ensures the system is easy to test, run, and understand.

---

### 🎯 Goals
- Add documentation headers to all code and script files
- Provide sample test input and CLI commands
- Create `.env-example` with required variables
- Validate CLI tool works end-to-end with expected output
- Document how to run and deploy locally

---

### 📋 Instructions for Codex Agent

#### 1. **Header Comments for Code Files**
Each `*.py` file in `agents/`, `tools/`, and `scripts/` must include:
```python
"""
Purpose: [Brief summary of what the file/agent/tool does]
Usage: Imported by agent runner or CLI
Deployment: Used in CLI or hosted apps (e.g. Streamlit, Railway)
Run: See `scripts/generate_user_stories.py`
"""
```

#### 2. **Script Headers (e.g. generate_user_stories.py)**
```python
"""
CLI for generating user stories from a feature idea
Run:
  python scripts/generate_user_stories.py
  or: poetry run python scripts/generate_user_stories.py
Deployment:
  Streamlit/Gradio UI (optional), or Railway CLI
Requirements:
  - Python 3.11+
  - `openai-agents[viz]`
  - `.env` file with OPENAI_API_KEY
"""
```

#### 3. **Test Data Setup**
- Add `data/sample_input.txt` with example feature:
  ```
  As a user, I want to upload a CSV of customer contacts to the CRM
  ```
- Optional: Add `expected_output_schema.yaml`

#### 4. **Test Instructions**
Document in `README.md` or script:
```bash
python scripts/generate_user_stories.py "As a user..."
open outputs/stories.json
open outputs/trace_graph.html
```

#### 5. **Environment Variables**
Create a `.env-example` file with:
```bash
# .env-example
OPENAI_API_KEY=your-api-key-here
```

#### 6. **Logging Enhancements**
- Integrate structured logging throughout all agents and tools using Python’s `logging` module.
- Include log messages for:
  - Agent/tool start and end
  - Input arguments and validation errors
  - Key decision points or branching logic
  - Trace and handoff progression
- Logging should output to both console and an optional `logs/agent_run.log` file (create directory if missing).
- Format logs as: `[LEVEL] [AgentName.ToolName] message`
- Set default log level to INFO with a CLI option for DEBUG

---

### ✅ Output
- Header comments added
- CLI documented
- Sample input file created
- Trace + result rendered
- `.env-example` created

---

This task improves onboarding, testability, and reproducibility for the PoC.