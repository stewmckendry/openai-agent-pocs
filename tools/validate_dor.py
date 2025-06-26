"""
Purpose: Validate that a story has required fields for DoR
Usage: Imported by agent runner or CLI
Deployment: Used in CLI or hosted apps (e.g. Streamlit, Railway)
Run: See `scripts/generate_user_stories.py`
"""

from agents import function_tool
import logging

logger = logging.getLogger(__name__)

@function_tool
def validate_dor(story: dict) -> bool:
    """Check if a story meets Definition of Ready (DoR)."""
    logger.debug("[validate_dor] called")
    required_fields = ["id", "title", "description"]
    return all(story.get(f) for f in required_fields)
