"""
Extra credits from proxycurl
"""

import requests

api_key = ''
headers = {'Authorization': 'Bearer ' + api_key}
api_endpoint = 'https://nubela.co/proxycurl/api/linkedin/profile/resolve'
params = {
    'company_domain': 'gatesfoundation.org',
    'first_name': 'Bill',
    'similarity_checks': 'include',
    'enrich_profile': 'enrich',
    'location': 'Seattle',
    'title': 'Co-chair',
    'last_name': 'Gates',
}
response = requests.get(api_endpoint,
                        params=params,
                        headers=headers)