import threading
import time


class Button:
    # Handle button presses

    alarm = None
    display = None

    def __init__(self, alarm, display):
        print "Init Button"
        self.alarm = alarm
        self.display = display

        thread = threading.Thread(target=self.timer)
        thread.daemon = True
        thread.start()

    def set_light(self, state):
        # TODO: actually switch light on and off
        if state:
            print "Button light on"
        else:
            print "Button light off"

    def timer(self):
        while True:
            # TODO: get actual hardware button state
            print "Check button"
            button_pressed = False
            if button_pressed:
                if self.alarm.is_alarm_sounding():
                    self.alarm.stop_alarm()
                else:
                    self.display.update_display(self.alarm.get_next_alarm())

            time.sleep(0.01)
