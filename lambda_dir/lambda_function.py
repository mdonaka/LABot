import os
import json
import requests
from datetime import date
from calender import GoogleCalendar
from decode import decode

def lambda_handler(event, context):
    URL = os.environ["WebhookURL"]
    ID = os.environ['GOOGLE_SERVICE_ACCOUNT_ID']
    URL = decode(URL)
    ID = decode(ID)

    calender = GoogleCalendar(ID)
    frm = date(year=2019, month=11, day=1).isoformat() + "T00:00:00.000000Z"
    to = date(year=2019, month=11, day=29).isoformat() + "T00:00:00.000000Z"
    schedule = calender.get_schedule(frm,to)

    text = schedule[0]
    requests.post(URL, data=json.dumps({
        'text': text
    }))
