# agents/human_approval_agent.py
from models.agent_state import AgentState
from langgraph.graph import END
from langchain_core.messages import HumanMessage
from .base_agent import BaseAgent

class HumanApprovalAgent(BaseAgent):
    def __init__(self):
        self._name = "human_approval"

    @property
    def name(self) -> str:
        return self._name

    def __call__(self, state: AgentState) -> AgentState:
        print("\n--- HUMAN REVIEW STEP ---")
        print("Generated Tool Code:\n")
        print(state.draft_tool_code)
        
        user_input = input("Approve this code? (yes/no): ").strip().lower()
        if user_input == "yes":
            state.human_approved_tool_code = True
            print("Human approved the code.")
            # Next step
            state.next_agent = "analyzer"
        else:
            print("Human did NOT approve. Provide modification instructions or press Enter to skip.")
            mod_instructions = input("Modification instructions: ")
            if mod_instructions:
                # This means we have new instructions from the human
                state.messages.append(HumanMessage(content=mod_instructions))
                state.human_approved_tool_code = False
                # Return to tool_creator for regeneration
                state.next_agent = "tool_creator"
            else:
                # If no instructions given, skip or consider next action
                state.human_approved_tool_code = False
                state.next_agent = "analyzer"  # Maybe skip changes
        return state
