import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API keys and credentials
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Load other necessary credentials like OpenAI API keys here
