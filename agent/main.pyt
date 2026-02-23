import speech_recognition as sr
import os
import webbrowser
import datetime
import pyttsx3
import sys
from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from sources import search_tool, wiki_tool, save_mth


# Load Environment
load_dotenv()

# Text to Speech
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def say(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()
# LangChain Setup
class codingassistant(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tool_used: list[str]

parser = PydanticOutputParser(pydantic_object=codingassistant)

llm = ChatOpenAI(model="gpt-3.5-turbo")

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are a coding assistant.
Answer the user query and use tools if needed.
{format_instructions}
            """,
        ),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}")
    ]
).partial(format_instructions=parser.get_format_instructions())

tools = [search_tool, wiki_tool, save_mth]

agent = create_tool_calling_agent(
    llm=llm,
    prompt=prompt,
    tools=tools
)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=False)


# AI Function 

def ai(prompt_text):
    try:
        raw_answer = agent_executor.invoke({"query": prompt_text})
        answer = parser.parse(raw_answer["output"])
        return f"{answer.topic}. {answer.summary}"
    except Exception:
        return "I am having trouble connecting to my servers."


# Speech Recognition

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        print("Listening...")
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language='en-US')
            print(f"User said: {query}")
            return query.lower()
        except Exception:
            return "none"

# Main Program
if __name__ == "__main__":
    say("System online")

    sites = [
        ["youtube", "https://www.youtube.com"],
        ["wikipedia", "https://www.wikipedia.org"],
        ["google", "https://www.google.com"],
        ["github", "https://www.github.com"],
        ["stack overflow", "https://stackoverflow.com"]
    ]

    while True:
        query = takecommand()

        if query == "none":
            continue

        # Open websites
        matched_site = False
        for site in sites:
            if f"open {site[0]}" in query:
                say(f"Opening {site[0]}")
                webbrowser.open(site[1])
                matched_site = True
                break

        if matched_site:
            continue

        # Time
        if "the time" in query:
            strTime = datetime.datetime.now().strftime("%I:%M %p")
            say(f"The time is {strTime}")

        # Windows apps
        elif "open camera" in query:
            os.system("start microsoft.windows.camera:")

        elif "open calculator" in query:
            os.system("calc")

        elif "open notepad" in query:
            os.system("notepad")

        # Exit
        elif "stop" in query or "exit" in query:
            say("Goodbye")
            sys.exit()

        # LangChain Agent
        else:
            response = ai(query)
            say(response)