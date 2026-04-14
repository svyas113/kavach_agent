# Kalash Packaging Customer Support Agent

An AI-powered customer support agent built with fastWorkflow for Kalash Packaging, a box and packaging manufacturer in Ahmedabad.

## 🚀 Quick Start

### 1. Virtual Environment (Already Set Up!)

The virtual environment is already created at `.venv` with all dependencies installed.

To activate it manually:
```bash
source .venv/bin/activate
```

Or use the helper script:
```bash
source activate.sh
```

### 2. Add Your API Key

**IMPORTANT:** Before training, add your API key to the configuration file:

```bash
nano box_support_agent/fastworkflow.passwords.env
```

Replace `your-mistral-api-key-here` with your actual API key.

**Get a free API key from:**
- [Mistral AI](https://mistral.ai) - for mistral-small model
- [OpenRouter](https://openrouter.ai) - for free GPT models

### 3. Train the Agent

```bash
./train.sh
```

This will:
- Generate synthetic training data
- Train intent detection models
- Create necessary model files

**Note:** Training may take 5-10 minutes on first run.

### 4. Run the Agent

```bash
./run.sh
```

The agent will start in interactive mode. You can then chat with it!

## 💬 Example Conversation

```
🤖 Welcome to Kalash Packaging, Customer! 👋

I'm your customer support assistant...

User > tell me about window boxes

🤖 **WINDOW BOXES**

**Top Window Range:**
   • 8x8x5 inch - Top window
   • 10x10x5 inch - Top window
   • 12x12x5 inch - Top window
...

User > I want 500 window boxes 10x10x5 with foil stamping

🤖 ✅ Added 500 x Window Box (10x10x5 Top Window) to your cart!
   📝 Notes: with foil stamping

User > show my cart

🤖 **Your Cart:**
1. Window Box: 10x10x5 Top Window x 500 (Notes: with foil stamping)

User > checkout

🤖 **ORDER SUMMARY FOR CUSTOMER**
[Complete order summary with contact info]
```

## 📁 Project Structure

```
.
├── box_support_agent/          # Main application
│   ├── application/            # Business logic
│   ├── _commands/              # Command definitions
│   ├── fastworkflow.env        # Configuration
│   ├── fastworkflow.passwords.env  # API keys ⚠️
│   └── README.md               # Detailed docs
│
├── .venv/                      # Virtual environment
├── requirements.txt            # Python dependencies
│
├── activate.sh                 # Activate venv
├── train.sh                    # Train the agent
├── run.sh                      # Run the agent
│
└── README.md                   # This file
```

## 🎯 What the Agent Does

- **Product Information**: Answers questions about window boxes, MDF boards, drum boards, cutlery kits
- **Shopping Cart**: Allows customers to add items with quantities and notes
- **Order Management**: View cart and checkout with complete summaries
- **Dynamic Pricing**: Informs customers that sales team will provide custom quotes
- **Natural Conversation**: Understands various ways of asking questions

## 🛠️ Technical Details

- **Framework**: fastWorkflow
- **Python Version**: 3.12.3 (requires 3.11+)
- **LLM**: Mistral Small (or your choice)
- **Architecture**: Class-based state management with context-aware commands

## 📦 Product Catalog

The agent has complete knowledge of:

### Window Boxes
- Top Window: 8x8x5, 10x10x5, 12x12x5 inch
- L Window: 10x10x5, 8x8x8, 10x10x8, 12x12x8 inch
- Features: Strong material, clean finish, pastel colors
- Customization: Foil stamping (MOQ 1000)

### MDF Boards
- Sizes: 6, 7, 8, 9, 10, 12, 14, 16, 18, 20, 14x19 inch
- Colors: White, Black, Golden, Pastel
- Shapes: Square (round corners), Round, Round with handle
- Custom branding available

### Drum Boards
- Sizes: 10x10, 12x12, 14x14
- Colors: Black, White, Golden

### Cutlery Kits
- Standard: 1 knife, 4 candles
- Customization: Branding available (MOQ 10,000)

## 🔧 Troubleshooting

### Training Fails
- Make sure you've added your API key in `box_support_agent/fastworkflow.passwords.env`
- Check your internet connection
- Verify the API key is valid

### Agent Not Responding Correctly
- Retrain the agent: `./train.sh`
- Check that training completed successfully
- Look for error messages in the output

### Virtual Environment Issues
- Recreate: `rm -rf .venv && python3 -m venv .venv`
- Reinstall: `source .venv/bin/activate && pip install -r requirements.txt`

## 📞 Contact

For Kalash Packaging:
- **Phone**: 9106845371, 7600337948
- **Location**: Ahmedabad
- **Products**: Bakery boxes, MDF boards, Drum boards, Cutlery kits

## 📝 Development

The application follows fastWorkflow best practices:
- Separation of business logic and commands
- Class-based state management
- Pydantic models for type safety
- Natural language understanding with intent detection

For detailed documentation, see:
- [box_support_agent/README.md](box_support_agent/README.md) - Complete guide
- [box_support_agent/PROJECT_SUMMARY.md](box_support_agent/PROJECT_SUMMARY.md) - Architecture overview
- [box_support_agent/QUICKSTART.md](box_support_agent/QUICKSTART.md) - Quick start guide

## 🎉 Features

✅ Natural language understanding
✅ Context-aware responses
✅ Shopping cart management
✅ Order summaries
✅ Product catalog from company brochure
✅ Dynamic pricing flow
✅ Professional checkout experience

---

Built with ❤️ using fastWorkflow
