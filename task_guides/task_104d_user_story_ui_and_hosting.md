## Task 104d: Build Web UI and Deploy User Story Agent

Create a simple professional web interface for testing the user story generation pipeline. Support both CLI and hosted (API) execution, and allow flexible resource inputs.

---

### 🎯 Objectives
- Enable users to test the pipeline via a form-based web UI
- Accept input from both local files (CLI) and web inputs (API)
- Deploy backend to Railway and frontend to Vercel

---

### 🖥️ UI Requirements (Frontend)
- Input field: `Feature description` (text)
- Optional fields:
  - `Tech Architecture (markdown)`
  - `Backlog Summary (markdown)`
  - `As-Is Design (markdown)`
- Button: **Draft User Story + Specs**
- Output display:
  - User story (markdown)
  - Specs (UX, functional, technical, etc. — optional)
  - Trace ID or live link
- Stack: React or Next.js with TailwindCSS
- Host via Vercel

---

### 🔧 Backend (API)
- Add `api/agent_pipeline.py` (FastAPI or Flask)
- Accept `POST /generate` with JSON payload:
  ```json
  {
    "feature": "...",
    "tech_architecture": "...",
    "backlog": "...",
    "as_is_design": "..."
  }
  ```
- Call into `DeliveryLead.run()` with injected resources (fallback to local file if missing)
- Return structured output and trace info

---

### 🔁 Local vs API Input Support
Update `DeliveryLeadAgent` and sub-agents to:
- Prefer passed-in resource text
- If missing, read from default file path (CLI usage)
Example:
```python
if provided_arch:
    context = provided_arch
else:
    context = Path("resources/tech_architecture.md").read_text()
```

---

### 🌐 Deployment
- **Railway (API)**:
  - Add `Procfile`: `web: uvicorn api.agent_pipeline:app --host 0.0.0.0 --port $PORT`
  - Configure `requirements.txt`, `pyproject.toml`
- **Vercel (Frontend)**:
  - Add `.env.production` for `AGENT_BACKEND_URL`
  - Expose a simple API proxy if needed for local testing

---

### 📂 Suggested Structure
```
pocs/user_story_agent/
├── web/
│   ├── client/ (React/Next.js frontend)
│   └── api/agent_pipeline.py (FastAPI)
```

---

### ✅ Output
- Working web app to test user story agents
- API-compatible with existing pipeline
- Deployed version usable by non-devs for PoC demo