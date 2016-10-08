import time
import threading
import datetime
import pygame


class Alarm:
    # Handle getting alarms and sounding them

    alarmIsSounding = False
    nextAlarm = None

    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load("cherub_rock.mp3")

        thread = threading.Thread(target=self.get_google_data)
        thread.daemon = True
        thread.start()

        self.nextAlarm = datetime.datetime.strptime('Oct 8 2016  7:39PM', '%b %d %Y %I:%M%p')

    def sound_alarm(self):
        pygame.mixer.music.play()
        self.nextAlarm = None
        self.alarmIsSounding = True

    def stop_alarm(self):
        pygame.mixer.music.stop()
        self.alarmIsSounding = False

    def get_next_alarm(self):
        return self.nextAlarm

    def is_alarm_sounding(self):
        return self.alarmIsSounding

    def get_google_data(self):
        while True:
            # print "Get alarm data from Google"
            # self.nextAlarm = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
            time.sleep(5)
