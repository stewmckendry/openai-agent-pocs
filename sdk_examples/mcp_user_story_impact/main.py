import asyncio
from pathlib import Path

from agents import Runner, gen_trace_id, trace
from agents.mcp import MCPServerStdio

from pocs.user_story_agent.agent.impact_agent import build_impact_agent


async def run(server):
    agent = build_impact_agent(server)
    message = "List the context files and summarize the project backlog."
    result = await Runner.run(agent, message)
    print(result.final_output)


async def main():
    context_dir = Path(__file__).resolve().parents[1] / "pocs" / "user_story_agent" / "resources" / "context_files"

    async with MCPServerStdio(
        name="Filesystem Server",
        params={"command": "npx", "args": ["-y", "@modelcontextprotocol/server-filesystem", str(context_dir)]},
    ) as server:
        trace_id = gen_trace_id()
        with trace("impact_mcp_example", trace_id=trace_id):
            print(f"View trace: https://platform.openai.com/traces/trace?trace_id={trace_id}\n")
            await run(server)


if __name__ == "__main__":
    asyncio.run(main())
