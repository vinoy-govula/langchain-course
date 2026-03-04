from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_openai import ChatOpenAI
# from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage
from tavily import TavilyClient
import os


load_dotenv()

# tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
tavily = TavilyClient()

@tool
def search(query: str) -> str:
    """
    Tool that searches over internet
    Args:
        query: The query to search for
    Returns:
        The search results
    """
    print(f"Searching for: {query}")
    return tavily.search(query=query)


# llm = ChatOpenAI(model="gpt-5", temperature=0)
llm = ChatOllama(model="gpt-oss-safeguard", temperature=0, max_retries=1)
tools = [search]  # [search]

agent = create_agent(model=llm, tools=tools)

def main():
    print("Welcome to the Search Agent!")
    result = agent.invoke({"messages":HumanMessage(content="Search for 3 job postings for an AI engineer using LangChain in Australia on LinkedIn and list their details")})
    print(result)


if __name__ == "__main__":
    main()

