"""I have no money lol!
   So wrote a Script to hit endpoints to earn extra credits on proxycurl"""

import requests

api_key = ''
headers = {'Authorization': 'Bearer ' + api_key}
api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
params = {
    'twitter_profile_url': 'https://x.com/johnrmarty/',
}
response = requests.get(api_endpoint,
                        params=params,
                        headers=headers)

