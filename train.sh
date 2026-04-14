#!/bin/bash
# Train the Kalash Packaging customer support agent

echo "🚀 Training the customer support agent..."
echo ""

# Activate virtual environment
source .venv/bin/activate

# Check if API key is configured
if grep -q "your-mistral-api-key-here" box_support_agent/fastworkflow.passwords.env; then
    echo "⚠️  WARNING: You need to add your API key first!"
    echo ""
    echo "Edit box_support_agent/fastworkflow.passwords.env and add your API key."
    echo "Get a free API key from:"
    echo "  - Mistral AI: https://mistral.ai"
    echo "  - OpenRouter: https://openrouter.ai"
    echo ""
    exit 1
fi

# Run training
fastworkflow train \
    ./box_support_agent \
    ./box_support_agent/fastworkflow.env \
    ./box_support_agent/fastworkflow.passwords.env

echo ""
echo "✅ Training complete!"
echo ""
echo "To run the agent, execute:"
echo "  ./run.sh"
