from typing import List
from pydantic import BaseModel, Field

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_openai import ChatOpenAI
# from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage
# from tavily import TavilyClient
# import os
from langchain_tavily import TavilySearch

class Source(BaseModel):
    """Represents the source of a search result"""
    url: str = Field(..., description="The URL of the source")

class AgentResponse(BaseModel):
    """Represents the response from the agent"""
    answer: str = Field(..., description="The answer from the agent")
    sources: List[Source] = Field(..., default_factory=list, description="The list of sources of the search result")

load_dotenv()

llm = ChatOpenAI(model="gpt-5", temperature=0)
# llm = ChatOllama(model="gpt-oss-safeguard", temperature=0, max_retries=1)
tools = [TavilySearch()]  # [search]

agent = create_agent(model=llm, tools=tools, response_format=AgentResponse)

def main():
    print("Welcome to the Search Agent!")
    result = agent.invoke(
        {
            "messages":HumanMessage(
                content="Search for 3 job postings for an AI engineer using LangChain in Australia on LinkedIn and list their details"
                )
            }
            )
    print(result)


if __name__ == "__main__":
    main()

