#!/bin/bash
# Simple test runner for run_coach_agent PoC

SCRIPT_DIR="$(dirname "$0")"
GOAL_FILE="$SCRIPT_DIR/sample_goal.txt"

python -m pocs.run_coach_agent.main < "$GOAL_FILE"

