from utils.helpers import get_gemini_response

def summarize_text(text):
    """
    Uses Gemini to summarize a given text.
    """
    prompt = f"Summarize the following information in a concise and clear way:\n\n{text}"
    return get_gemini_response(prompt)
