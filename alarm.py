import time
import threading
import datetime


class Alarm:
    # Handle getting alarms and sounding them

    alarmIsSounding = False
    nextAlarm = None

    def __init__(self):
        # Nothing yet - will initialise display as in light_sensor.py
        print "Init Alarm"
        thread = threading.Thread(target=self.get_google_data)
        thread.daemon = True
        thread.start()

        self.nextAlarm = datetime.datetime.strptime('Oct 17 2016  6:59PM', '%b %d %Y %I:%M%p')

    def sound_alarm(self):
        # TODO: start the alarm sound
        self.alarmIsSounding = True
        print "Sounding alarm"

    def stop_alarm(self):
        # TODO: stop the alarm sound
        self.alarmIsSounding = False
        print "Stopping alarm"

    def get_next_alarm(self):
        return self.nextAlarm

    def is_alarm_sounding(self):
        return self.alarmIsSounding

    def get_google_data(self):
        while True:
            # print "Get alarm data from Google"
            # self.nextAlarm = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
            time.sleep(5)
