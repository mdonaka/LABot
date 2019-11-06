
import httplib2
from googleapiclient import discovery
from oauth2client.service_account import ServiceAccountCredentials
import os


class GoogleCalendar(object):

    def __init__(self, ID):
        self.service_account_id = ID

    def get_credentials(self):
        scopes = 'https://www.googleapis.com/auth/calendar'
        json = 'google_key.json'

        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            json,
            scopes=scopes
        )

        return credentials


    def get_schedule(self, time_min, time_max):
        try:
            credentials = self.get_credentials()
            http = credentials.authorize(httplib2.Http())
            service = discovery.build(
                'calendar',
                'v3',
                http=http
            )

            calendar_id = self.service_account_id
            events = service.events().list(
                calendarId=calendar_id,
                timeMin=time_min,
                timeMax=time_max,
                singleEvents=True
            ).execute()

            items = events['items']

            return [item["summary"] for item in items]

        except Exception as e:
            print(e)


