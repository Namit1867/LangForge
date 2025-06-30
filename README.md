# 🚀 LangForge

## 📌 Overview

**LangForge** is a robust AI-powered framework designed to automate the creation of **LangChain-compatible tools** through a modular **multi-agent system**. This framework enables users to define, modify, and generate custom tools leveraging pre-existing **LangChain** capabilities, retrieving external knowledge, and integrating **human-in-the-loop approval** to ensure the highest standards of quality.

Built on **LangGraph**, a stateful workflow framework, this system orchestrates multiple intelligent agents, each handling specialized tasks, to streamline tool creation and optimization.

---

## 🏗️ Project Architecture

The project follows a **highly modular architecture**, integrating **object-oriented principles (OOP)** to enhance maintainability, scalability, and extensibility. Each agent encapsulates specific responsibilities, ensuring clean separation of concerns and streamlined debugging.

```
LangGraphCustomToolBuilder/
├── README.md           # Project documentation (this file)
├── requirements.txt    # List of dependencies
├── main.py             # Main entry point to run the workflow
├── agents/             # Individual AI agent classes
│   ├── base_agent.py
│   ├── tool_explorer_agent.py
│   ├── research_agent.py
│   ├── reasoning_agent.py
│   ├── tool_creator_agent.py
│   ├── human_approval_agent.py
│   ├── analyzer_agent.py
│   └── writer_agent.py
├── models/             # Pydantic-based data models
│   └── agent_state.py
├── workflows/          # Graph-based workflow management
│   └── create_workflow.py
└── tools/              # Generated and predefined tools
    ├── __init__.py
    ├── custom_search_tool.py
    └── custom_calculator_tool.py
```

---

## 🔥 Core Features

### 🛠️ Automated Custom Tool Generation
- Generates **LangChain-compatible** tools based on user input.
- Utilizes **LLM-powered reasoning** for intelligent tool structuring.
- Supports **multiple tool types**, including search tools, API clients, and computational tools.

### 🤖 AI-Driven Multi-Agent Workflow
- Implements **LangGraph** to define structured **stateful workflows**.
- Each agent performs specialized roles such as research, reasoning, code generation, validation, and documentation.
- **Human-in-the-loop intervention** allows users to refine generated tools before finalization.

### 🌍 Web & API Integration
- Supports **external web scraping, API calls, and knowledge retrieval**.
- Dynamically identifies **third-party dependencies** required for tool execution.
- Integrates **pre-existing LangChain tools** when applicable.

### 🔄 Memory & Checkpointing
- Utilizes **LangGraph's memory checkpointing** for seamless workflow continuity.
- Allows restarting from the last saved state in case of interruptions.

### ⚡ Modular & OOP-Compliant Codebase
- **Encapsulated agent design** following **Single Responsibility Principle (SRP)**.
- Clear **separation of concerns** for scalability and easy maintenance.
- Supports **custom workflow modifications** via `create_workflow.py`.

---

## 🤖 Multi-Agent Workflow Breakdown

Each agent in the workflow executes a specific function, contributing to the seamless generation of tools.

### **1️⃣ Tool Explorer Agent**
🔍 **Analyzes User Request & Identifies Relevant Tools**
- Determines whether an **existing LangChain tool** is sufficient or a new tool must be created.
- Loads **pre-existing tools** and categorizes them based on functionality.

### **2️⃣ Research Agent**
📚 **Retrieves External Information**
- Uses **LLM-driven analysis** to gather references, APIs, and dependencies.
- Stores research findings within `AgentState`.

### **3️⃣ Reasoning Agent**
🧠 **Performs Structured Step-by-Step Reasoning**
- Breaks down tool requirements into a structured implementation plan.
- Ensures **input/output consistency** with LangChain’s tool framework.

### **4️⃣ Tool Creator Agent**
📝 **Generates LangChain-Compatible Python Code**
- Uses **LLM-powered code synthesis** to create a new tool.
- Implements **synchronous and asynchronous execution methods**.

### **5️⃣ Human Approval Agent**
🛑 **Human-in-the-Loop Verification**
- Allows manual review of generated code.
- Provides options to **approve, modify, or regenerate** code based on feedback.

### **6️⃣ Analyzer Agent**
🔬 **Validates & Enhances Code Quality**
- Checks for **syntax errors, missing docstrings, and optimization opportunities**.
- Suggests **error handling improvements**.

### **7️⃣ Writer Agent**
📜 **Finalizes Tool Documentation & Storage**
- Stores finalized tool in `tools/`.
- Generates supplementary documentation, including:
  - **Code structure overview**
  - **Research insights**
  - **Tool dependencies**
  - **Potential enhancements**

---

## 🛠️ Installation & Setup

### 🔹 Prerequisites
- Python 3.8+
- OpenAI API key for LLM-powered agents

### 🔹 Install Dependencies
```sh
pip install -r requirements.txt
```

### 🔹 Configure Environment Variables
Create a `.env` file:
```sh
OPENAI_API_KEY=your-api-key-here
```

### 🔹 Run the Workflow
```sh
python main.py
```

---

## 📦 Example Usage

### 🔹 User Input Request
```yaml
User Request: "Create a custom Wikipedia search tool."
```

### 🔹 Generated Tool Example
```python
from typing import Optional, Type
from pydantic import BaseModel, Field
from langchain.tools import BaseTool

class WikipediaSearchInput(BaseModel):
    query: str = Field(description="The search term for Wikipedia.")

class WikipediaSearchTool(BaseTool):
    name = "wikipedia_search"
    description = "Search Wikipedia articles based on a given query."
    args_schema: Type[BaseModel] = WikipediaSearchInput

    def _run(self, query: str) -> str:
        """Perform Wikipedia search."""
        return f"Mock Wikipedia search result for: {query}"

    async def _arun(self, query: str) -> str:
        """Asynchronous execution is not supported."""
        raise NotImplementedError("Wikipedia search does not support async")
```

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 📞 Contact

👤 **Author**: Namit Jain  
📧 **Email**: [namit.cs.rdjps@gmail.com](mailto:namit.cs.rdjps@gmail.com)  
🔗 **LinkedIn**: [https://www.linkedin.com/in/namit-jain-355367186/](https://www.linkedin.com/in/namit-jain-355367186/)

---

## 🎯 Future Enhancements

- [ ] **Integration with Vector Databases** for tool indexing.
- [ ] **Support for additional tool types** (e.g., image processing, speech recognition).
- [ ] **Advanced multi-agent collaboration** to handle complex workflows.
- [ ] **Automated API documentation generation** for each tool.

🚀 **Empower AI-Driven Tool Development with LangGraph!** 🎉

