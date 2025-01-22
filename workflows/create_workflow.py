# workflows/create_workflow.py

from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver
from models.agent_state import AgentState

# Import your agents
from agents.tool_explorer_agent import ToolExplorerAgent
from agents.research_agent import ResearchAgent
from agents.reasoning_agent import ReasoningAgent
from agents.tool_creator_agent import ToolCreatorAgent
from agents.analyzer_agent import AnalyzerAgent
from agents.writer_agent import WriterAgent
from agents.human_approval_agent import HumanApprovalAgent

def create_agent_workflow(llm):
    """
    Build the workflow with all agents in a StateGraph.
    """
    # Initialize agent instances
    tool_explorer = ToolExplorerAgent()
    researcher = ResearchAgent(llm)
    reasoning_agent = ReasoningAgent(llm)
    tool_creator = ToolCreatorAgent(llm)
    analyzer = AnalyzerAgent()
    writer = WriterAgent()
    human_approval = HumanApprovalAgent()

    # Create the workflow and memory checkpoint
    workflow = StateGraph(AgentState)
    memory = MemorySaver()

    # Add nodes (each node is an agent)
    workflow.add_node(tool_explorer.name, tool_explorer)
    workflow.add_node(researcher.name, researcher)
    workflow.add_node(reasoning_agent.name, reasoning_agent)
    workflow.add_node(tool_creator.name, tool_creator)
    workflow.add_node(analyzer.name, analyzer)
    workflow.add_node(writer.name, writer)
    workflow.add_node(human_approval.name, human_approval)

    # Define edges
    workflow.add_edge("tool_explorer", "researcher")
    workflow.add_edge("researcher", "reasoning_agent")
    workflow.add_edge("reasoning_agent", "tool_creator")
    # After tool creation, we can route to human approval if code not approved
    workflow.add_edge("tool_creator", human_approval.name)
    workflow.add_edge(human_approval.name, "tool_creator")  # loop back if modified
    workflow.add_edge(human_approval.name, "analyzer")      # or proceed to analyzer
    workflow.add_edge("analyzer", "writer")
    workflow.add_edge("writer", END)

    # Set the entry point
    workflow.set_entry_point("tool_explorer")

    # Compile with a memory checkpointer
    compiled_workflow = workflow.compile(checkpointer=memory)
    return compiled_workflow
