class RunUnitTestsTool:
    """Simulate running unit tests."""
    name = "run_unit_tests"

    def __call__(self, code: str):
        # pretend to run tests
        return {"success": True, "details": "All unit tests passed"}
