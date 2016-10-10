import time
import threading
import pygame


class Alarm:
    """ Handle getting alarms and sounding them
    """

    alarmIsSounding = False
    nextAlarm = None
    api = None

    def __init__(self, api):
        """ Get the next alarm time, and start a background thread to get new alarm times
        """
        self.api = api
        self.nextAlarm = self.api.get_next_alarm_event()

        thread = threading.Thread(target=self.__get_google_data)
        thread.daemon = True
        thread.start()

    def sound_alarm(self):
        """ Sound an alarm
        """
        pygame.mixer.init()
        pygame.mixer.music.load("cherub_rock.mp3")
        pygame.mixer.music.play()

        self.nextAlarm = None
        self.alarmIsSounding = True

    def stop_alarm(self):
        """ Stop an alarm from sounding
        """
        pygame.mixer.music.stop()
        pygame.mixer.quit()

        self.alarmIsSounding = False

    def get_next_alarm(self):
        """ Property accessor to get the next alarm time set
        """
        return self.nextAlarm

    def is_alarm_sounding(self):
        """ Property accessor to check if the alarm is sounding
        """
        return self.alarmIsSounding

    def __get_google_data(self):
        """ Background thread to periodically get the next alarm time
        """
        while True:
            self.nextAlarm = self.api.get_next_alarm_event()
            time.sleep(60)
