from agents.search_agent import search_web
from agents.fact_checker import fact_check
from agents.summarizer import summarize_text
import os
from langgraph.graph import Graph, END

os.environ["GRPC_VERBOSITY"] = "NONE"
os.environ["GRPC_ENABLE_FORK_SUPPORT"] = "0"

if __name__ == "__main__":
 


    query = input("Enter your query: ")

    # Initialize the graph
    workflow = Graph()

    # Add nodes (using existing function names)
    workflow.add_node("search", search_web)
    workflow.add_node("fact_check", fact_check)
    workflow.add_node("summarize", summarize_text)

    # Define the execution flow
    workflow.set_entry_point("search")
    workflow.add_edge("search", "fact_check")
    workflow.add_edge("fact_check", "summarize")
    workflow.add_edge("summarize", END)

    # Compile the graph
    graph_executor = workflow.compile()

    # Run the pipeline
    final_state = graph_executor.invoke({"query": query})

# Check the actual returned dictionary structure
    print("🔍 Debugging Final Output")

# Extract summary correctly
    if "summary" in final_state:
        print("🔹 Final Summary:", final_state["summary"])
    elif "fact_check_result" in final_state and isinstance(final_state["fact_check_result"], dict):
        if "summary" in final_state["fact_check_result"]:
            print("🔹 Final Summary:", final_state["fact_check_result"]["summary"])
        else:
            print("Summary key missing in fact_check_result")
    else:
        print("Summary not found in final output")

