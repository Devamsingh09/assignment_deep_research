from tavily import TavilyClient
from utils.config import TAVILY_API_KEY

# Initialize Tavily client
tavily_client = TavilyClient(api_key=TAVILY_API_KEY)

def search_web(input_data):
    print("Function search_web called.")  

    if not isinstance(input_data, dict) or "query" not in input_data:
        raise ValueError("Expected input_data to be a dictionary with a 'query' key.")
    
    query = input_data["query"].strip()  
    print(f"🔍 Searching for: {query}") 

    if not query:
        raise ValueError("Query must be a non-empty string.")

 
    search_results = tavily_client.search(query=query)
    return {"search_results": search_results}
