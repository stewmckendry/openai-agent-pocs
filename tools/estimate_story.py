"""
Purpose: Tool returning a static story point estimate
Usage: Imported by agent runner or CLI
Deployment: Used in CLI or hosted apps (e.g. Streamlit, Railway)
Run: See `scripts/generate_user_stories.py`
"""

from openai_agents import traceable
from openai_agents.tools import tool
import logging

logger = logging.getLogger(__name__)

@traceable
@tool
def story_estimate(story: dict) -> int:
    """Return a fixed story point estimate."""
    logger.debug("[story_estimate] called")
    return 3
