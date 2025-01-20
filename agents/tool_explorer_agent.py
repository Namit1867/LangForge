# agents/tool_explorer_agent.py
from typing import Dict, List
from langchain.tools import BaseTool
from langchain_community.agent_toolkits.load_tools import load_tools
from models.agent_state import AgentState
from .base_agent import BaseAgent

class ToolExplorerAgent(BaseAgent):
    def __init__(self):
        self._name = "tool_explorer"
        self.tool_categories = [
            "requests",
            "python",
            "shell",
            "gmail",
            "google_search",
            "wikipedia"
        ]

    @property
    def name(self) -> str:
        return self._name

    def _load_available_tools(self) -> Dict[str, List[BaseTool]]:
        available_tools = {}
        for category in self.tool_categories:
            try:
                # load_tools returns a list of tools for that category
                tools = load_tools([category])
                available_tools[category] = tools
            except Exception:
                continue  # If a tool cannot be loaded, skip it
        return available_tools

    def _analyze_tool_requirements(self, query: str) -> List[str]:
        """
        Simple heuristic to detect relevant tool categories from the query.
        """
        tool_keywords = {
            "web": ["requests", "google_search"],
            "research": ["wikipedia", "google_search"],
            "local": ["python", "shell"],
            "communication": ["gmail"]
        }
        needed_tools = []
        lower_query = query.lower()
        for keyword, tools in tool_keywords.items():
            if keyword in lower_query:
                needed_tools.extend(tools)
        # Remove duplicates
        return list(set(needed_tools))

    def __call__(self, state: AgentState) -> AgentState:
        query = state.messages[-1].content if state.messages else ""
        # Load all tools
        state.available_tools = self._load_available_tools()
        needed_tool_categories = self._analyze_tool_requirements(query)

        # For demonstration, let's store these categories somewhere
        state.research_results["tool_suggestions"] = needed_tool_categories
        # Mark progress
        state.task_status["tool_exploration"] = "completed"
        # Decide next step
        state.next_agent = "researcher"
        return state
