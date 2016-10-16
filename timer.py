import threading
import datetime
import time
import pytz


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

        thread = threading.Thread(target=self.__timer)
        thread.daemon = True
        thread.start()

    def __timer(self):
        """ Background thread to update the time and sound the alarm
        """
        while True:
            # Alarm times from Google are in UTC, but we want to display the local time.
            display_time = datetime.datetime.now()
            utc_time = datetime.datetime.now(pytz.utc)
            self.display.update_display(display_time.strftime("%I%M").lstrip('0'))

            if self.alarm.get_next_alarm() is not None and utc_time > self.alarm.get_next_alarm():
                self.button.set_light(True)
                self.alarm.sound_alarm()

            time.sleep(1)
