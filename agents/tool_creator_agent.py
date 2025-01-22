# agents/tool_creator_agent.py
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from models.agent_state import AgentState
from .base_agent import BaseAgent

class ToolCreatorAgent(BaseAgent):
    def __init__(self, llm: ChatOpenAI):
        self._name = "tool_creator"
        self.llm = llm
        self.prompt = PromptTemplate(
            template="""You are a code-generation agent. 
User wants a new tool for: "{query}"
We have these summarized findings and reasoning:
{research_and_reasoning}
Available tool references or categories: {tools}

Generate Python code for a new tool class or function that is 
LangChain-compatible (i.e., extends BaseTool or similar) to meet the user's request EXACTLY. 
Output only the code, no extra commentary.
""",
            input_variables=["query", "research_and_reasoning", "tools"]
        )

    @property
    def name(self) -> str:
        return self._name

    def __call__(self, state: AgentState) -> AgentState:
        query = state.messages[-1].content if state.messages else ""
        reasoning = state.research_results.get("reasoning", "")
        research_findings = state.research_results.get("current", {}).get("findings", "")
        
        # Gather tool names (if any)
        tool_list = []
        for cat, cat_tools in state.available_tools.items():
            for t in cat_tools:
                tool_list.append(t.name)
        tools_desc = ", ".join(tool_list) if tool_list else "None"

        prompt_text = self.prompt.format(
            query=query,
            research_and_reasoning=f"{research_findings}\n{reasoning}",
            tools=tools_desc
        )

        # Send to the LLM for code generation with LangChain compatibility
        response = self.llm(prompt_text, ensure_langchain_compatibility=True)
        code_snippet = response.content

        # The user might want JSON or direct code. For now, store as string:
        state.draft_tool_code = code_snippet
        state.task_status["tool_creation"] = "code_generated"

        # We'll let the workflow handle next_agent (conditional)
        return state
