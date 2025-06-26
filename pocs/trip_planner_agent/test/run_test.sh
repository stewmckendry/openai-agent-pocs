#!/bin/bash
# Simple test runner for trip_planner_agent PoC

SCRIPT_DIR="$(dirname "$0")"
INPUT_FILE="$SCRIPT_DIR/sample_input.txt"

python -m pocs.trip_planner_agent.main < "$INPUT_FILE"
