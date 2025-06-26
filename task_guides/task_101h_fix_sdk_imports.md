## Task 101h: Fix Imports and Naming to Match SDK Structure

Ensure all SDK imports align with the latest published OpenAI Agents SDK usage. Codex Agents should not alias or guess imports — use SDK entrypoints directly.

---

### 🎯 Goals
- Fix incorrect import paths across agents, tools, and runners
- Remove outdated or aliased forms like `from agents.tools import tool`
- Match SDK documentation and usage from examples

---

### ✅ Correct Import Patterns
Use these patterns directly:

```python
from agents import Agent, ModelSettings, function_tool

@function_tool
def get_weather(city: str) -> str:
    return f"The weather in {city} is sunny"

agent = Agent(
    name="Haiku agent",
    instructions="Always respond in haiku form",
    model="o3-mini",
    tools=[get_weather],
)
```

```python
from agents import Agent, FileSearchTool, Runner, WebSearchTool

agent = Agent(
    name="Assistant",
    tools=[
        WebSearchTool(),
        FileSearchTool(max_num_results=3, vector_store_ids=["VECTOR_STORE_ID"]),
    ],
)

async def main():
    result = await Runner.run(agent, "Which coffee shop should I go to today?")
    print(result.final_output)
```

```python
from typing_extensions import TypedDict, Any
from agents import Agent, FunctionTool, RunContextWrapper, function_tool

class Location(TypedDict):
    lat: float
    long: float

@function_tool
async def fetch_weather(location: Location) -> str:
    return "sunny"

@function_tool(name_override="fetch_data")
def read_file(ctx: RunContextWrapper[Any], path: str, directory: str | None = None) -> str:
    return "<file contents>"

agent = Agent(
    name="Assistant",
    tools=[fetch_weather, read_file],
)
```

```python
from agents import Agent, function_tool
from agents.extensions.visualization import draw_graph

@function_tool
def get_weather(city: str) -> str:
    return f"The weather in {city} is sunny."

spanish_agent = Agent(name="Spanish agent", instructions="You only speak Spanish.")
english_agent = Agent(name="English agent", instructions="You only speak English")

triage_agent = Agent(
    name="Triage agent",
    instructions="Handoff to the appropriate agent based on the language of the request.",
    handoffs=[spanish_agent, english_agent],
    tools=[get_weather],
)

draw_graph(triage_agent)
```

```python
from agents import Agent, Runner, trace

agent = Agent(name="Joke generator", instructions="Tell funny jokes.")

with trace("Joke workflow"):
    first = await Runner.run(agent, "Tell me a joke")
    second = await Runner.run(agent, f"Rate this: {first.final_output}")
```

---

### 🔍 Instructions
- Codex Agent should audit and update every file in `agents/`, `tools/`, and `scripts/`
- Check for aliases like `from agents.tools import tool` — fix them all
- If unsure about symbol, check `src/agents/` in SDK repo for canonical source

---

### 📘 Reference Sources
- https://github.com/openai/openai-agents-python/blob/main/docs/tools.md
- https://github.com/openai/openai-agents-python/blob/main/docs/tracing.md
- https://github.com/openai/openai-agents-python/blob/main/docs/visualization.md
- https://github.com/openai/openai-agents-python/tree/main/examples

---

### ✅ Output
- Correct SDK imports across the repo
- Patch log saved to `task_guides/reports/task_101h_import_fixes_report.md`