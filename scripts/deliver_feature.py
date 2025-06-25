#!/usr/bin/env python
"""CLI entry for running the delivery workflow."""
import argparse
import json
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent))
from workflows.delivery_orchestration import run_delivery_flow


def main():
    parser = argparse.ArgumentParser(description="Run delivery agents")
    parser.add_argument("feature", help="Feature idea text")
    parser.add_argument("--use-search", action="store_true", help="Enable web search in review")
    parser.add_argument("--out", default="project/outputs", help="Output directory")
    args = parser.parse_args()

    results, trace = run_delivery_flow(args.feature, use_search=args.use_search)

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "results.json", "w") as f:
        json.dump(results, f, indent=2)
    with open(out_dir / "trace.json", "w") as f:
        json.dump(trace, f, indent=2)
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
