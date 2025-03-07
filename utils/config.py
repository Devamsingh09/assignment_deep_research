import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API Keys
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

# Ensure API keys are available
if not GOOGLE_API_KEY or not TAVILY_API_KEY:
    raise ValueError("Missing API keys! Please add them to the .env file.")
