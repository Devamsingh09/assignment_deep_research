from agents.search_agent import search_web
from agents.fact_checker import fact_check
from agents.summarizer import summarize_text
import os

os.environ["GRPC_VERBOSITY"] = "NONE"
os.environ["GRPC_ENABLE_FORK_SUPPORT"] = "0"


if __name__ == "__main__":
    query = "Tell me about stampede in maha kumbh 2025?"
    
    # Step 1: Fetch information
    raw_info = search_web(query)
    
    # Step 2: Fact-check the retrieved information
    fact_checked_info = fact_check(str(raw_info))

    # Step 3: Summarize the fact-checked content
    summary = summarize_text(fact_checked_info)

    print("🔹 Final Summary:", summary)
