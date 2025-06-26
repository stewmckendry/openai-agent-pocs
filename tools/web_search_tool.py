from openai_agents.tools import tool

@tool
def web_search(query: str):
    """Mock web search returning static results."""
    return f"Results for '{query}': example best practices."
