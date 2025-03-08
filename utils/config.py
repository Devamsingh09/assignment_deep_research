import os
from dotenv import load_dotenv

# Loading environment variables from .env file
load_dotenv()

# API Keys (load from environment)
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

# Ensuring API keys are available
if not GOOGLE_API_KEY or not TAVILY_API_KEY:
    raise ValueError("Missing API keys! Please check your .env file.")

# Debug
print(f"✅ GOOGLE_API_KEY Loaded: {GOOGLE_API_KEY[:5]}...")
print(f"✅ TAVILY_API_KEY Loaded: {TAVILY_API_KEY[:5]}...")
