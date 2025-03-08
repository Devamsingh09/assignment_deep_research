from utils.helpers import get_gemini_response
import logging

def summarize_text(input_data):
    print("🔍 Debugging Input to summarize_text")  
    
    if not isinstance(input_data, dict) or "text" not in input_data:
        raise ValueError(f"Expected input_data to be a dictionary with a 'text' key. Got: {input_data}")

    text = input_data["text"]
    prompt = f"Summarize the following text efficiently:\n\n{text}"

    try:
        summary_text = get_gemini_response(prompt)
        return {"summary": summary_text}
    except Exception as e:
        logging.error(f"Error while getting summary: {e}")
        return {"error": "Failed to get summary"}
