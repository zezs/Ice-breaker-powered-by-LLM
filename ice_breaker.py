from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
import os
from third_parties.linkedin import scrape_linkedin_profile 

load_dotenv()


if __name__ == "__main__":

    print("Hello Langchain")
    # creating promt template
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

    # call
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url="https://www.linkedin.com/in/eden-marco/", mock=True)

    #executing chain using invoke method and passing i/p parameter "information"
    res = chain.invoke(input={"information": linkedin_data})

    print(res.content)