import threading
import time
import RPi.GPIO as GPIO


class Button:
    """ Handle button presses and the button light
    """

    alarm = None
    display = None
    pin_button_signal = 15
    pin_button_light = 14

    def __init__(self, alarm, display):
        """" Initialise the pins for the button light and signal
             Start the background thread to monitor for button presses
        """

        self.alarm = alarm
        self.display = display

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin_button_light, GPIO.OUT)
        GPIO.setup(self.pin_button_signal, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        thread = threading.Thread(target=self.__timer)
        thread.daemon = True
        thread.start()

    def set_light(self, state):
        """ Set the state of the button light
            True = turn the light on
            False = turn the light off
        """
        if state:
            GPIO.output(self.pin_button_light, GPIO.HIGH)
        else:
            GPIO.output(self.pin_button_light, GPIO.LOW)

    def __timer(self):
        """ Background thread to monitor for button presses
        """
        while True:
            # Slightly confusingly, my wiring means that pressing the button gives
            # False on the input
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
