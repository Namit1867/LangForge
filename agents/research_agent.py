# agents/research_agent.py
from langchain import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from models.agent_state import AgentState
from .base_agent import BaseAgent

class ResearchAgent(BaseAgent):
    def __init__(self, llm: ChatOpenAI):
        self._name = "researcher"
        self.llm = llm
        self.prompt = PromptTemplate(
            template="""You are a research agent. A user wants to build a tool.
User request: {query}

We have these tools available:
{tools}

Previous partial findings:
{previous_findings}

Brainstorm relevant considerations, references, or APIs needed for building the new tool. 
Return your findings as a short summary with bullet points.""",
            input_variables=["query", "tools", "previous_findings"]
        )

    @property
    def name(self) -> str:
        return self._name

    def __call__(self, state: AgentState) -> AgentState:
        query = state.messages[-1].content if state.messages else ""
        previous = state.research_results.get("tool_suggestions", [])
        # Build a textual list of tools
        tool_list = []
        for cat, cat_tools in state.available_tools.items():
            for t in cat_tools:
                tool_list.append(t.name)
        tools_desc = ", ".join(tool_list) if tool_list else "None"

        # Format the input
        chain_input = {
            "query": query,
            "tools": tools_desc,
            "previous_findings": previous
        }

        # Use the LLM
        chain_of_thought = self.llm(self.prompt.format(**chain_input))
        
        # Store results
        state.research_results["current"] = {
            "timestamp": "2025-01-14",  # Example date
            "findings": chain_of_thought.content
        }

        # Next agent
        state.next_agent = "reasoning_agent"
        return state
