#!/usr/bin/env python
"""CLI entry for running the SDK-based delivery workflow."""
import argparse
import json
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent))
from workflows.delivery_orchestration import run_delivery_flow


def main():
    parser = argparse.ArgumentParser(description="Run delivery agents")
    parser.add_argument("feature", nargs="?", help="Feature idea text")
    parser.add_argument("--use-search", action="store_true", help="Enable web search in review")
    parser.add_argument("--out", default="project/outputs", help="Output directory")
    args = parser.parse_args()

    feature = args.feature or input("Enter feature idea: ")
    results, trace = run_delivery_flow(feature, use_search=args.use_search)

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "results.json", "w") as f:
        json.dump(results, f, indent=2)
    trace_path = out_dir / "trace.json"
    with open(trace_path, "w") as f:
        json.dump(trace.serialize(), f, indent=2)

    # visualize if available
    try:
        from openai_agents.visualization import visualize_trace

        visualize_trace(trace, out_dir / "trace_graph.html")
    except Exception:
        pass

    print(json.dumps(results, indent=2))
    print(f"Trace saved to {trace_path} with id: {trace.id}")


if __name__ == "__main__":
    main()
