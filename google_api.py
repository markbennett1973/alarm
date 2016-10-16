import httplib2

from apiclient import discovery
from oauth2client.file import Storage

import datetime
import dateutil.parser


class GoogleApi:
    """ Get events from the Google Calendar API
    """
    SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
    CLIENT_SECRET_FILE = 'client_secret.json'
    APPLICATION_NAME = 'Alarm Pi'

    credentials = None

    def __init__(self):
        """ Get valid user credentials from storage.
        """
        store = Storage('google-credentials.json')
        self.credentials = store.get()
        if not self.credentials or self.credentials.invalid:
            raise ValueError('Google API credentials invalid or not found - run google_auth.py in a desktop environment')

    def get_next_alarm_event(self):
        """ Get the next event from the calendar with the title "Alarm"
        """
        http = self.credentials.authorize(httplib2.Http())
        service = discovery.build('calendar', 'v3', http=http)

        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        events_result = service.events().list(
            calendarId='primary', timeMin=now, maxResults=10, singleEvents=True,
            orderBy='startTime').execute()
        events = events_result.get('items', [])

        if events:
            for event in events:
                start = event['start'].get('dateTime', event['start'].get('date'))
                if event['summary'] == 'Alarm':
                    return dateutil.parser.parse(start)
