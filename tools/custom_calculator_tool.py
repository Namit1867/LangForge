# tools/custom_calculator_tool.py
from typing import Optional, Type
from pydantic import BaseModel, Field
from langchain.callbacks.manager import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
)
from langchain.tools import BaseTool

class CalculatorInput(BaseModel):
    a: int = Field(description="First number.")
    b: int = Field(description="Second number.")

class CustomCalculatorTool(BaseTool):
    name = "Calculator"
    description = "Useful for mathematics or numerical tasks."
    args_schema: Type[BaseModel] = CalculatorInput
    return_direct: bool = True

    def _run(
        self, a: int, b: int, run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> str:
        """Perform multiplication operation."""
        return str(a * b)

    async def _arun(
        self, a: int, b: int, run_manager: Optional[AsyncCallbackManagerForToolRun] = None
    ) -> str:
        """Asynchronous run method."""
        raise NotImplementedError("Calculator does not support async")
