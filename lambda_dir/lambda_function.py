import os
import json
import requests

def lambda_handler(event, context):
    URL = os.environ["WebhookURL"]
    requests.post(URL, data=json.dumps({
        'text': u'Hello World From Python.'
    }))
