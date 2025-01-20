# agents/writer_agent.py
from models.agent_state import AgentState
from .base_agent import BaseAgent

class WriterAgent(BaseAgent):
    def __init__(self):
        self._name = "writer"

    @property
    def name(self) -> str:
        return self._name

    def __call__(self, state: AgentState) -> AgentState:
        analysis = state.research_results.get("analysis", {})
        # The final output is the code plus optional summary
        state.final_output = {
            "title": "Generated Tool Code",
            "tool_code": state.draft_tool_code,
            "analysis": analysis
        }
        state.next_agent = "END"
        return state
