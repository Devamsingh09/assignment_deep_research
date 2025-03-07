from tavily import TavilyClient
from utils.config import TAVILY_API_KEY

# Initialize Tavily client
tavily_client = TavilyClient(api_key=TAVILY_API_KEY)

def search_web(query):
    """
    Uses Tavily API to fetch relevant web search results.
    """
    search_results = tavily_client.search(query=query)
    return search_results
