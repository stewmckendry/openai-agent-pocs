"""ResearchAgent executes web searches for trip planning topics."""

from pathlib import Path
from pydantic import BaseModel
from agents import Agent, ModelSettings, WebSearchTool


class ResearchSummary(BaseModel):
    """Concise search summary."""

    summary: str


def _load_prompt() -> str:
    path = Path(__file__).resolve().parent.parent / "prompts" / "research_prompt.yaml"
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return "".join(lines[1:]).lstrip()


research_agent = Agent(
    name="ResearchAgent",
    instructions=_load_prompt(),
    tools=[WebSearchTool()],
    model_settings=ModelSettings(tool_choice="required"),
    output_type=ResearchSummary,
)
