import os, sys
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI #llm
from langchain.prompts.prompt import PromptTemplate
from langchain_core.tools import Tool 
from langchain.agents import (
    create_react_agent, # Method: create_react_agent is a method used to init a ReAct agent, equipped with necesssary tools, llm and prompt
    AgentExecutor, # Object: manages execution which recives user prompt, tools and executes our task by invoking all required func
)
from langchain import hub # provides with premade prompts by langchain community
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tools.tools import get_profile_url_tavily 
load_dotenv()




def lookup(name: str)-> str:
    llm = ChatOpenAI(temperature=0, model_name= "gpt-3.5-turbo")

    # !!!refer output indicator: help us get only url as the answer
    template = """given the full name {name_of_person} I want you to get me a link to their Linkedin Profile page, Your anser should only contain a URL"""
    prompt_template = PromptTemplate(template=template, input_variable=["name_of_person"])

    tools_for_agent = [
        Tool(
            name="Crawl Google for linkedin profile page", func=get_profile_url_tavily, description="Useful for when you need to get the Linkedin Page URL"
            )
    ]

    react_prompt = hub.pull("hwchase17/react") # react prompting -> sent to llm (incl. tools, tool names and their uses)
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt) # 
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True) # invoking all the python func 
    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name_of_person=name)}
    )

    linkedin_profile_url = result["output"]
    return linkedin_profile_url


if __name__ == "__main__":
    linkedin_url = lookup(name="Eden Marco")
    print(linkedin_url)