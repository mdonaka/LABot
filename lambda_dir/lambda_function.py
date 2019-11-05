import os
import json
import requests
# from decode import decode

def lambda_handler(event, context):
    URL = os.environ["WebhookURL"]
    # URL = decode(URL)
    requests.post(URL, data=json.dumps({
        'text': u'Hello World From AWS.'
    }))
