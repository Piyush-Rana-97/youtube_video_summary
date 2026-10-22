from agno.agent import Agent

from agno.models.openai import OpenAIResponses
from agno.models.groq import Groq

from dotenv import load_dotenv

from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.hackernews import HackerNewsTools
from agno.tools.websearch import WebSearchTools

load_dotenv()

def build_agent():
    return Agent(
        model=Groq(id="openai/gpt-oss-120b"),
        # model=Groq(id="qwen/qwen3-32b"),
        tools=[DuckDuckGoTools(), HackerNewsTools(), WebSearchTools()],
        markdown=True,
        instructions="You are a helpful and expert travel agent.",
        add_datetime_to_context=True
    )

agent = build_agent()

# agent.print_response("My budget is 1L INR, should I travel to Goa or Phuket?")
# agent.print_response("What is tomorrow date?")
# agent.print_response("What is your knowledge cutoff?")
agent.print_response("Is it safe to travel to Iran today?")