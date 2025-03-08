import google.generativeai as genai
from utils.config import GOOGLE_API_KEY

# Configuring Gemini API
genai.configure(api_key=GOOGLE_API_KEY)

def get_gemini_response(prompt):
    """
    Calls Google Gemini 1.5 Pro and returns the response.
    """
    model = genai.GenerativeModel("gemini-1.5-pro")
    response = model.generate_content(prompt)
    return response.text  # Extract text from response
