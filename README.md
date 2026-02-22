***AI Coding Assistant Agent***

An intelligent tool-calling AI agent built with LangChain that can search the web, retrieve knowledge, generate structured coding assistance, and persist results locally.

This project demonstrates a production-style LLM agent architecture using structured outputs, external tools, and environment-based configuration.

Built with:

LangChain

OpenAI

**Why This Project?**

This project demonstrates:

Tool orchestration

Structured outputs (Pydantic)

External knowledge retrieval

Persistent storage

Environment-based security

**Modular architecture**

This follows a real-world agent pattern:

LLM + Tools + Validation + Persistence

**Features**

Coding assistance and summaries

Web search (DuckDuckGo)

Wikipedia knowledge retrieval

Structured JSON output using Pydantic

Save responses with timestamps

Secure API key management using .env

Modular and scalable design

**Architecture**
User Query
     ↓
LangChain Agent
     ↓
Tool Selection
     ↓
LLM Processing (OpenAI)
     ↓
Pydantic Output Validation
     ↓
Save to File

Core Pattern:

Retrieval + Knowledge + Memory

Project Structure
AI-Coding-Assistant/
│
├── main.py               # Agent execution
├── sources.py            # Tools (search, wiki, save)
├── chathistory.txt       # Stored outputs
├── requirements.txt      # Dependencies
├── .env                  # API keys (not committed)
└── README.md
Installation
1. Clone Repository
git clone https://github.com/Eamon2009/AI-Agent-plus.git
cd AI-Coding-Assistant
2. Create Virtual Environment

**Windows**

python -m venv venv
venv\Scripts\activate

**Linux / Mac**

python3 -m venv venv
source venv/bin/activate
Why use a virtual environment?

Isolates project dependencies

Prevents version conflicts

Keeps system Python clean

Makes the project reproducible

Python development always uses virtual environments.

3. Install Dependencies

Create requirements.txt

langchain
langchain-openai
langchain-community
pydantic
python-dotenv
duckduckgo-search
wikipedia

Install:

pip install -r requirements.txt

4. Setup Environment Variables

Create a .env file:

OPENAI_API_KEY=your_openai_api_key_here

Get your API key:

https://platform.openai.com/api-keys

OpenAI Platform:

https://platform.openai.com/

LangChain Documentation:

https://python.langchain.com/

Run the Project
python main.py

Then enter your query:

Enter what do you want to build:

The agent will:

Use tools if needed

Generate structured output

Save results to chathistory.txt

**Imports Overview**
main.py
from dotenv import load_dotenv

from pydantic import BaseModel

from langchain_openai import ChatOpenAI

from langchain_core.prompts import ChatPromptTemplate

from langchain_core.output_parsers import PydanticOutputParser

from langchain.agents import create_tool_calling_agent, AgentExecutor

from sources import search_tool, wiki_tool, save_mth

sources.py

from langchain_community.utilities import WikipediaAPIWrapper

from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun, Tool

from datetime import datetime

Example Output
{
  topic: "Flask API",
  summary: "Steps to build a Flask API...",
  sources: ["Wikipedia", "Web Search"],
  tool_used: ["search", "wiki"]
}

**Future Improvements**

Conversation memory (LangChain Memory)

Error handling and retries

Streaming responses

FastAPI or Streamlit interface

Multi-model support (OpenAI + Anthropic)

Vector database integration

**Use Cases**

Learning LangChain

Agent architecture reference

Prototype for AI applications
