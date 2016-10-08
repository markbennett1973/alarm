import threading
import time
import RPi.GPIO as GPIO


class Button:
    # Handle button presses

    alarm = None
    display = None
    pin_button_signal = 15
    pin_button_light = 14

    def __init__(self, alarm, display):
        self.alarm = alarm
        self.display = display

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin_button_light, GPIO.OUT)
        GPIO.setup(self.pin_button_signal, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        thread = threading.Thread(target=self.timer)
        thread.daemon = True
        thread.start()

    def set_light(self, state):
        if state:
            GPIO.output(self.pin_button_light, GPIO.HIGH)
        else:
            GPIO.output(self.pin_button_light, GPIO.LOW)

    def timer(self):
        while True:
            if not GPIO.input(self.pin_button_signal):
                if self.alarm.is_alarm_sounding():
                    self.set_light(False)
                    self.alarm.stop_alarm()
                    time.sleep(2)

                else:
                    alarm_time = self.alarm.get_next_alarm()
                    if alarm_time is not None:
                        self.display.update_display(alarm_time.strftime("%I%M").lstrip('0'))

            time.sleep(0.01)
