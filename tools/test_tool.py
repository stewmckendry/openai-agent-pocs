"""
Purpose: Dummy tool simulating a unit test run
Usage: Imported by agent runner or CLI
Deployment: Used in CLI or hosted apps (e.g. Streamlit, Railway)
Run: See `scripts/generate_user_stories.py`
"""

from agents import function_tool
import logging

logger = logging.getLogger(__name__)

@function_tool
def run_unit_tests(code: str):
    """Simulate running unit tests."""
    logger.debug("[run_unit_tests] called")
    return {"success": True, "details": "All unit tests passed"}
