from openai_agents.tools import tool

@tool
def story_estimate(story: dict) -> int:
    """Return a fixed story point estimate."""
    return 3
