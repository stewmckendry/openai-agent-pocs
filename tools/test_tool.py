from openai_agents.tools import tool

@tool
def run_unit_tests(code: str):
    """Simulate running unit tests."""
    return {"success": True, "details": "All unit tests passed"}
