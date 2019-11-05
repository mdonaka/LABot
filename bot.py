import json
import requests

with open("data.json", "r") as f:
    data = json.load(f)
    URL = data["WebhookURL"]
    requests.post(URL, data=json.dumps({
        'text': u'Hello World From Python.'
    }))
