# highly optimised search API for genai workloads
from langchain_community.tools.tavily_search import TavilySearchResults
from dotenv import load_dotenv

load_dotenv()


def get_profile_url_tavily(name:str):
    """ Searches Linkedin profile """
    search = TavilySearchResults()
    res = search.run(f"{name}")
    return res[0]["url"]