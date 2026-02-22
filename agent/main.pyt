from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from sources import search_tool,wiki_tool,save_mth

load_dotenv()
language_model_1 = ChatOpenAI(model="gpt-3.5-turbo")# i am using GPT 3.5 
#language_Model_2=ChatAnthropic(model="claude-4-0-sonnet") you can use any model you want 
class codingassistant(BaseModel):
       topic:str
       summary:str
       sources:list[str]
       tool_used:list[str]
parser=PydanticOutputParser(pydantic_object=codingassistant)
prompt=ChatPromptTemplate.from_messages(
       [
              (
              "system",
              """
              You are a coding assistant that help generate code.
              Answer users query and use neccessary tools.
              Wrape the output in this format and provide no other text \n(format_instructions)
 
              """,
              ),
              ("placeholder","{chat_history}"),
              ("Human","{query}"),
              ("placeholder","{agent_scratchpad}")
       ]
).partial(format_instructions=parser.get_format_instructions())
tools=[search_tool,wiki_tool,save_mth]
agent=create_tool_calling_agent(
       language_model_1=language_model_1,
       prompt=prompt,
       tools=tools
       
)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=False)#verbose=True,if you want to see the process
query=input("Enter what do you want to build:")
raw_answer=agent_executor.invoke({"query":query})# Add any question in place of query  to test
#print(raw_answer)
try:
       answer = parser.parse(raw_answer["output"])
       print(answer)
except Exception as e:
       print("Sorry something went wrong !!")
       print(e,raw_answer)

