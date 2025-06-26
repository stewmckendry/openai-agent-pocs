from openai_agents import traceable
from openai_agents.tools import tool

@traceable
@tool
def impact_assessment(story: dict) -> str:
    """Simple tool to assess impact on existing systems."""
    return "Minimal impact on current architecture."
