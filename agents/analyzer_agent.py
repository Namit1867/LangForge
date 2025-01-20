# agents/analyzer_agent.py
from models.agent_state import AgentState
from .base_agent import BaseAgent

class AnalyzerAgent(BaseAgent):
    def __init__(self):
        self._name = "analyzer"

    @property
    def name(self) -> str:
        return self._name

    def __call__(self, state: AgentState) -> AgentState:
        code = state.draft_tool_code
        # Basic analysis logic here
        analysis = {
            "syntax_check": "No syntax errors found (hypothetical).",
            "improvements": "Add docstrings or handle exceptions properly."
        }
        state.research_results["analysis"] = analysis
        state.task_status["analysis"] = "completed"
        # Next
        state.next_agent = "writer"
        return state
