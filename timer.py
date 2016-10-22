import threading
import datetime
import time
import pytz
import logging


class Timer:
    """ Handle the main clock timer loop
    """
    display = None
    alarm = None
    button = None

    def __init__(self, display, alarm, button):
        """ Start the background thread to manage the time
        """
        self.display = display
        self.alarm = alarm
        self.button = button

        logging.info('Timer:init')
        thread = threading.Thread(target=self.__timer)
        thread.daemon = True
        thread.start()

    def __timer(self):
        """ Background thread to update the time and sound the alarm
        """
        while True:
            # Alarm times from Google are in UTC, but we want to display the local time.
            display_time = datetime.datetime.now().strftime("%I%M").lstrip('0')
            utc_time = datetime.datetime.now(pytz.utc)
            logging.debug('Timer:updating time to %s', display_time)
            self.display.update_display(display_time)

            if self.alarm.get_next_alarm() is not None and utc_time > self.alarm.get_next_alarm():
                logging.debug('Timer:sound alarm')
                self.button.set_light(True)
                self.alarm.sound_alarm()

            time.sleep(1)
