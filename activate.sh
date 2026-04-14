#!/bin/bash
# Activation script for the virtual environment

source .venv/bin/activate
echo "✅ Virtual environment activated!"
echo "Python version: $(python --version)"
echo "fastworkflow installed at: $(which fastworkflow)"
echo ""
echo "To train the agent, run:"
echo "  ./train.sh"
echo ""
echo "To run the agent, run:"
echo "  ./run.sh"
