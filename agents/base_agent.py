# agents/base_agent.py
from abc import ABC, abstractmethod
from models.agent_state import AgentState

class BaseAgent(ABC):
    """Optional base class for all agents to maintain consistency."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Name or identifier for the agent."""
        pass

    @abstractmethod
    def __call__(self, state: AgentState) -> AgentState:
        """Executes the agent logic."""
        pass
