# main.py
import os
from langchain_openai import ChatOpenAI
from workflows.create_workflow import create_agent_workflow
from models.agent_state import AgentState
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()

def run_agent_team(query: str, thread_id: str):
    """Runs the compiled agent workflow from entry to end, returning final output."""
    llm = ChatOpenAI(model="gpt-4o", temperature=0, api_key=os.getenv("OPENAI_API_KEY"))  # Use ChatGPT 4 (or another chat model)
    workflow = create_agent_workflow(llm)
    
    # Initialize the state with the user's query
    state = AgentState(messages=[HumanMessage(content=query)])
    
    # Provide config with thread_id
    config = {"configurable": {"thread_id": thread_id}}
    
    final_state = workflow.invoke(state, config=config)
    return final_state.final_output

if __name__ == "__main__":
    user_query = "Create a custom search tool that queries Wikipedia for the latest information."
    thread_id = "unique_thread_123"
    result = run_agent_team(user_query, thread_id)
    print("\n=== FINAL OUTPUT ===")
    print(result)
