"""
Purpose: Tool to provide a mock impact assessment result
Usage: Imported by agent runner or CLI
Deployment: Used in CLI or hosted apps (e.g. Streamlit, Railway)
Run: See `scripts/generate_user_stories.py`
"""

from agents import function_tool
import logging

logger = logging.getLogger(__name__)

@function_tool
def impact_assessment(story: dict) -> str:
    """Simple tool to assess impact on existing systems."""
    logger.debug("[impact_assessment] called")
    return "Minimal impact on current architecture."
