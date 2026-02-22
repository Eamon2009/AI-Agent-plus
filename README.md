AI Coding Assistant Agent

An intelligent coding assistant built with LangChain that can search the web, retrieve knowledge, generate structured responses, and save results locally.

This project demonstrates a practical tool-calling AI agent architecture using modern LLM workflows.

Badges
Python 3.9+ | LangChain | OpenAI API | Pydantic | Virtual Environment
Overview

The AI Coding Assistant can:

Generate coding guidance and explanations

Search the web using DuckDuckGo

Retrieve information from Wikipedia

Return structured output using Pydantic

Save responses to a local file with timestamps

Use environment variables for secure API handling

Built using:

LangChain

OpenAI

Project Structure
AI-Coding-Assistant/
│
├── main.py               # Main agent execution
├── sources.py            # Tools (search, wiki, save)
├── chathistory.txt       # Stored outputs
├── .env                  # API keys (ignored in Git)
├── requirements.txt      # Dependencies
└── README.md
Requirements

Python 3.9 or higher

OpenAI API Key

Get your API key:
https://platform.openai.com/api-keys

LangChain documentation:
https://python.langchain.com/

Step 1 — Create Virtual Environment
Windows
python -m venv venv
venv\Scripts\activate
Linux / Mac
python3 -m venv venv
source venv/bin/activate
Why Virtual Environment?

Keeps project dependencies isolated

Avoids version conflicts

Keeps system Python clean

Makes the project portable and reproducible

Step 2 — Install Dependencies

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
Step 3 — Environment Setup

Create a .env file:

OPENAI_API_KEY=your_openai_api_key_here
Step 4 — Run the Project
python main.py

Then enter your query:

Enter what do you want to build:

The agent will:

Use tools if required

Generate structured output

Save results to chathistory.txt

Imports Used
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
Output Format

The assistant returns structured data:

{
  topic: string
  summary: string
  sources: list
  tool_used: list
}
Architecture Flow

User Input
→ LangChain Agent
→ Tool Selection
→ LLM Processing
→ Pydantic Validation
→ File Storage

This follows a practical pattern:

Retrieval + Knowledge + Persistence

Future Improvements

Conversation memory

Error handling and retries

Streaming responses

Web interface (FastAPI / Streamlit)

Multi-model support

Use Cases

Learning AI agent development

LangChain practice project

Prototype for larger AI applications


“Why this project is different” section

If you want, I can create a README V2 that looks like a top AI engineer’s repository — that will make your project stand out strongly.
