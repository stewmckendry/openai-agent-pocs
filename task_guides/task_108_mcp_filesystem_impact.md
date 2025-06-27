## Task 108: Use MCP Filesystem Server in PoC1 for Impact Assessment

Refactor `ImpactAssessmentAgent` in PoC1 (UserStoryAgent) to use the OpenAI MCP Filesystem server to access context files instead of reading hardcoded file paths.

---

### 🎯 Goal
Enable the agent to:
- Dynamically discover files in `resources/context_files/`
- Use the MCP SDK to load and reason over file contents

---

### 🧠 Why This Matters
- Avoids hardcoding file I/O logic
- Reusable pattern for any agent needing structured file access
- Enables dynamic reasoning over a set of project context files

---

### 🔧 Instructions for Codex Agent
- You MUST use the SDK:
  ```python
  from agents import Agent, Runner, gen_trace_id, trace
  from agents.mcp import MCPServer, MCPServerStdio
  ```
- You MUST NOT define your own MCP tool wrappers
- You MUST follow the live example in:
  ```
  examples/mcp_filesystem/main.py
  ```
- Your impact agent should:
  - Accept the MCP server as an input to its constructor or runner
  - Search for design/code/backlog insights using LLM prompting
  - Use output as `ImpactAssessmentOutput`

---

### 🧩 What to Build
1. **Agent Refactor**
   - `agent/impact_agent.py`: Add `mcp_servers=[server]` to agent constructor
   - Add prompt logic to guide how to use file contents
2. **Example MCP Server**
   - Add script or CLI wrapper to launch Filesystem server using `npx`
   - Point it to `resources/context_files/` (ensure it exists)
3. **Trace Integration**
   - Wrap execution in `with trace(...):`
   - Log trace_id and agent output

---

### 📘 Setup Instructions
To run the MCP Filesystem server, install:
```bash
npm install -g npx
```
Then:
```bash
npx -y @modelcontextprotocol/server-filesystem path/to/resources/context_files
```

---

### ✅ Output
- `ImpactAssessmentAgent` can scan, read, and reason from live file context
- No hardcoded file reads remain
- Trace + output fully captured for verification

This improves modularity, extensibility, and opens the door to HostedMCPTool usage later.