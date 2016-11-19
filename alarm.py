import time
import threading
import pygame
import logging


class Alarm:
    """ Handle getting alarms and sounding them
    """

    alarmIsSounding = False
    nextAlarm = None
    api = None
    alarmVolumeThread = None

    def __init__(self, api):
        """ Get the next alarm time, and start a background thread to get new alarm times
        """
        self.api = api
        self.nextAlarm = self.api.get_next_alarm_event()

        logging.info('Alarm:init')

        thread = threading.Thread(target=self.__get_google_data)
        thread.daemon = True
        thread.start()

        self.alarmVolumeThread = threading.Thread(target=self.__increase_alarm_volume())

    def sound_alarm(self):
        """ Sound an alarm
        """
        logging.debug('Alarm:sounding alarm')
        pygame.mixer.init()
        pygame.mixer.music.load("alarm.mp3")
        pygame.mixer.music.play()

        # Volume will be increased by the increaseVolume thread
        pygame.mixer.music.set_volume(0)

        self.nextAlarm = None
        self.alarmIsSounding = True

        self.alarmVolumeThread.start()

    def stop_alarm(self):
        """ Stop an alarm from sounding
        """
        logging.debug('Alarm:stopping alarm')
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
            logging.debug('Alarm:getting next alarm event')
            self.nextAlarm = self.api.get_next_alarm_event()
            time.sleep(300)

    def __increase_alarm_volume(self):
        while self.alarmIsSounding:
            pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.1)
            time.sleep(10)
