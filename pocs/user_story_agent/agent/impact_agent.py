"""Impact assessment agent using the MCP filesystem server."""

from pathlib import Path
from pydantic import BaseModel
from agents import Agent
from agents.mcp import MCPServer


class ImpactSummary(BaseModel):
    """Summary of expected code and documentation impact."""

    summary: str


def _load_prompt() -> str:
    path = Path(__file__).resolve().parent.parent / "prompts" / "impact_prompt.yaml"
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return "".join(lines[1:]).lstrip()


def build_impact_agent(server: MCPServer) -> Agent:
    """Create an ImpactAssessmentAgent that can access context files via MCP."""

    return Agent(
        name="ImpactAssessmentAgent",
        instructions=_load_prompt(),
        mcp_servers=[server],
        output_type=ImpactSummary,
    )


__all__ = ["ImpactSummary", "build_impact_agent"]
