from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
lang_key = os.getenv("LANGSMITH_API_KEY")

# Turn LangSmith tracking ON
os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_API_KEY"] = lang_key
os.environ["LANGSMITH_PROJECT"] = "LangSmith-Project"          # runs are grouped under this name
os.environ["OPENAI_API_KEY"] = api_key

print("LangSmith is connected!")

from langchain_openai import ChatOpenAI 
llm = ChatOpenAI(model="gpt-4o-mini")

prompts = ["I want to learn about AI and Python", 
           "Give me a detail plan and schedule to learn AI and Python", 
           "What is the career path for AI and Python"] 

for p in prompts: response = llm.invoke(p)
print(f"Prompt: {p}\nResponse: {response.content}\n")

