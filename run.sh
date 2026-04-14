#!/bin/bash
# Run the Kalash Packaging customer support agent

echo "🤖 Starting the customer support agent..."
echo ""

# Activate virtual environment
source .venv/bin/activate

# Check if trained
if [ ! -d "box_support_agent/___command_info" ]; then
    echo "⚠️  Agent not trained yet!"
    echo ""
    echo "Please run the training first:"
    echo "  ./train.sh"
    echo ""
    exit 1
fi

# Run the agent
fastworkflow run \
    ./box_support_agent \
    ./box_support_agent/fastworkflow.env \
    ./box_support_agent/fastworkflow.passwords.env \
    --startup_action ./box_support_agent/startup_action.json

echo ""
echo "👋 Thanks for using the Kalash Packaging support agent!"
