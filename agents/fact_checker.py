from utils.helpers import get_gemini_response

def fact_check(input_data):
    if not isinstance(input_data, dict) or "search_results" not in input_data:
        raise ValueError("Expected input_data to be a dictionary with 'search_results' key.")

    statement = input_data["search_results"]
    prompt = f"Verify the truthfulness of the following statement and return only reliable information provide a confidence level:\n\n{statement}"

    fact_check_result = get_gemini_response(prompt)

    return {"text": fact_check_result} 
