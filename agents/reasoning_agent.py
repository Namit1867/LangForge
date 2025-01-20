# agents/reasoning_agent.py
from langchain_openai import ChatOpenAI
from models.agent_state import AgentState
from .base_agent import BaseAgent

class ReasoningAgent(BaseAgent):
    def __init__(self, llm: ChatOpenAI):
        self._name = "reasoning_agent"
        self.llm = llm

    @property
    def name(self) -> str:
        return self._name

    def __call__(self, state: AgentState) -> AgentState:
        query = state.messages[-1].content if state.messages else ""
        findings = state.research_results.get("current", {}).get("findings", "")

        prompt = f"""User request: {query}\nResearch Findings: {findings}\n
Please provide a step-by-step reasoning on how to build the requested tool and the potential approach to code generation.
"""

        response = self.llm(prompt)
        state.research_results["reasoning"] = response.content
        state.task_status["reasoning"] = "completed"
        state.next_agent = "tool_creator"
        return state
