"""
Purpose: Mock web search tool returning canned results
Usage: Imported by agent runner or CLI
Deployment: Used in CLI or hosted apps (e.g. Streamlit, Railway)
Run: See `scripts/generate_user_stories.py`
"""

from openai_agents.tools import tool
import logging

logger = logging.getLogger(__name__)

@tool
def web_search(query: str):
    """Mock web search returning static results."""
    logger.debug("[web_search] called with %s", query)
    return f"Results for '{query}': example best practices."
