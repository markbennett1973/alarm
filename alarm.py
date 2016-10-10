import time
import threading
import pygame


class Alarm:
    # Handle getting alarms and sounding them

    alarmIsSounding = False
    nextAlarm = None
    api = None

    def __init__(self, api):
        self.api = api
        self.nextAlarm = self.api.get_next_alarm_event()

        thread = threading.Thread(target=self.get_google_data)
        thread.daemon = True
        thread.start()

    def sound_alarm(self):
        pygame.mixer.init()
        pygame.mixer.music.load("cherub_rock.mp3")
        pygame.mixer.music.play()

        self.nextAlarm = None
        self.alarmIsSounding = True

    def stop_alarm(self):
        pygame.mixer.music.stop()
        pygame.mixer.quit()

        self.alarmIsSounding = False

    def get_next_alarm(self):
        return self.nextAlarm

    def is_alarm_sounding(self):
        return self.alarmIsSounding

    def get_google_data(self):
        while True:
            self.nextAlarm = self.api.get_next_alarm_event()
            time.sleep(60)
