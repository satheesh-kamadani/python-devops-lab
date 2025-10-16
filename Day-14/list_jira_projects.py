# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
import os

url = "https://satheeshkamadani.atlassian.net/rest/api/3/project"

auth = HTTPBasicAuth(os.getenv("EMAIL"), os.getenv("API_TOKEN"))

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

data = response.json()
for project in data:
    print(project["name"])