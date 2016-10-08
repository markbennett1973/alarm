import threading
import datetime
import time


class Timer:
    # Handle displaying data on the LCD screen
    display = None
    alarm = None

    def __init__(self, display, alarm):
        print "Init Timer"
        self.display = display
        self.alarm = alarm

        thread = threading.Thread(target=self.timer)
        thread.daemon = True
        thread.start()

    def timer(self):
        while True:
            my_time = datetime.datetime.now()
            self.display.update_display(my_time.strftime("%I%M").lstrip('0'))

            if my_time > self.alarm.get_next_alarm():
                self.alarm.sound_alarm()

            time.sleep(1)
