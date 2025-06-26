from openai_agents.tools import tool

@tool
def impact_assessment(story: dict) -> str:
    """Simple tool to assess impact on existing systems."""
    return "Minimal impact on current architecture."
