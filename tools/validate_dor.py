from openai_agents import traceable
from openai_agents.tools import tool

@traceable
@tool
def validate_dor(story: dict) -> bool:
    """Check if a story meets Definition of Ready (DoR)."""
    required_fields = ["id", "title", "description"]
    return all(story.get(f) for f in required_fields)
