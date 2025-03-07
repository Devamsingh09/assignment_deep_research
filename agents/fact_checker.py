from utils.helpers import get_gemini_response

def fact_check(statement):
    """
    Uses Gemini to fact-check a given statement.
    """
    prompt = f"Verify the truthfulness of the following statement and provide a confidence level:\n\n{statement}"
    return get_gemini_response(prompt)
