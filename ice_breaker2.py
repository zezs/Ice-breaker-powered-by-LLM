from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
import os
from agents.Linkedin_lookup_agent import lookup as linkedin_lookup_agent
from third_parties.linkedin import scrape_linkedin_profile 

load_dotenv()


def break_ice_with(keywords:str) -> str:
    
    print("Extracting URL...")
    linkedin_url = linkedin_lookup_agent(keywords)
    print("URL Extracted:", linkedin_url)

    print("Scraping data from Linkedin Profile....")
    linkedin_data = scrape_linkedin_profile(linkedin_url)
    print("Scrapped Data:", linkedin_data)

    summary_template = """
    given the information {information} about a person from I want you to create:
        1. a short summary
        2. Profile pic url
        2. two intresting facts about the person
        3. How to pronounce his/her name
        """
    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)

    # creating model
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    # creating chain 
    chain = summary_prompt_template | llm

    #executing chain using invoke method and passing i/p parameter "information"
    res = chain.invoke(input={"information": linkedin_data})
    print(res.content)


if __name__ == "__main__":
    print("Welcome to Ice breaker powered by Generative AI.....")
    break_ice_with(keywords="Bill Gates")
   