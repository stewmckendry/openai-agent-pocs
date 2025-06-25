class WebSearchTool:
    """Mock web search returning static results."""
    name = "web_search"

    def __call__(self, query: str):
        return f"Results for '{query}': example best practices."
