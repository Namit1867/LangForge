# models/agent_state.py
from typing import Dict, List, Any, Union
from pydantic import BaseModel, Field
from langchain_core.messages import HumanMessage, AIMessage, BaseMessage  # hypothetical module
from langgraph.graph.message import add_messages

def merge_dicts(x: Dict[str, Any], y: Dict[str, Any]) -> Dict[str, Any]:
    merged = x.copy()
    merged.update(y)
    return merged

def overwrite_str(x: str, y: str) -> str:
    return y

def overwrite_bool(x: bool, y: bool) -> bool:
    return y

def conditional_overwrite_union(x: Union[str, None], y: Union[str, None]) -> Union[str, None]:
    """If y is not None, overwrite; otherwise keep x."""
    return y if y is not None else x

class AgentState(BaseModel):
    """Overall state to be passed between agents in the workflow."""
    messages: List[BaseMessage] = Field(default_factory=list, description="All the conversation messages so far.")
    next_agent: Union[str, None] = Field(default="tool_explorer")
    task_status: Dict[str, str] = Field(default_factory=dict)
    research_results: Dict[str, Any] = Field(default_factory=dict)
    final_output: Dict[str, Any] = Field(default_factory=dict)
    available_tools: Dict[str, Any] = Field(default_factory=dict)
    draft_tool_code: str = ""
    human_approved_tool_code: bool = False
