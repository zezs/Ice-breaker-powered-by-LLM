import os
import requests
from dotenv import load_dotenv

load_dotenv()

def scrape_linkedin_profile(linkedin_profile_url:str, mock = False):
    
    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/emarco177/0d6a3f93dd06634d95e46a2782ed7490/raw/78233eb934aa9850b689471a604465b188e761a0/eden-marco.json"
        response = requests.get(
            linkedin_profile_url,
            timeout = 10,
        )
    
    else:
        api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
        header_dic = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}
        response = requests.get(
            api_endpoint,
            params={"url": linkedin_profile_url},
            headers = header_dic,
            timeout=10,
        )
    
    data = response.json()

    # Filter out unwanted key-value pairs
    filtered_data = {}
    for k, v in data.items():
        if v not in ([], "", None) and k not in ["people_also_viewed", "certifications"]:
            filtered_data[k] = v

    # Remove profile pictures from groups if present
    if "groups" in filtered_data:
        for group in filtered_data["groups"]:
            group.pop("profile_pic_url", None)

    return filtered_data



if __name__ == "__main__":
    print("Extracting linedin profile data.......")
    # print(scrape_linkedin_profile(linkedin_profile_url="https://www.linkedin.com/in/eden-marco/"))