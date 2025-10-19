from flask import Flask
import requests
from requests.auth import HTTPBasicAuth
import json

# Create a flask app instance
app = Flask(__name__)

@app.route("/createJIRA", methods="POST")
def createJIRA():

    url = "https://satheeshkamadani.atlassian.net/rest/api/3/issue"

    API_TOKEN = ""

    auth = HTTPBasicAuth("", API_TOKEN)

    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

    payload = json.dumps( {
    "fields": {
        "description": {
        "content": [
            {
            "content": [
                {
                "text": "My own project first task",
                "type": "text"
                }
            ],
            "type": "paragraph"
            }
        ],
        "type": "doc",
        "version": 1
        },
        "issuetype": {
        "id": "10024"
        },
        "project": {
        "key": "SS"
        },
        "summary": "My own project first task",
    },
    "update": {}
    } )
    
    response = requests.request(
    "POST",
    url,
    data=payload,
    headers=headers,
    auth=auth
    )

app.run('0.0.0.0', port=5000)