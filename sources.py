from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools import WikipediaQueryRun ,DuckDuckGoSearchRun
from  langchain_community.tools import Tool
from datetime import datetime

s=DuckDuckGoSearchRun()
search_tool=Tool(
       name="search",
       function=s.run,
       description="search the web for information",
)
api_wrapper=WikipediaAPIWrapper(top_k_results=2,doc_content_chars_max=1000)
wiki_tool=WikipediaQueryRun(api_wrapper=api_wrapper)

def chat_history(data:str,filename:str="chathistory.txt"):
       timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
       savetext=(f"----Result----\nTimestamp:{timestamp}\n{data}\n")
       
       with open(filename,"a",encoding="utf-8") as f:
              f.write(savetext)
       
       return (f"chat sucessfully saved to file : {filename}")
save_mth = Tool(
    name="save_text_to_file",
    func=chat_history,
    description="Save text data to a file with timestamp",
)




