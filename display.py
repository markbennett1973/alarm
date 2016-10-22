from Adafruit_LED_Backpack import SevenSegment
import light_sensor
import logging


class Display:
    """ Handle displaying data on the LCD screen
    """
    display = None
    sensor = None

    def __init__(self):
        """ Initialise the LCD display
        """
        self.display = SevenSegment.SevenSegment()
        self.sensor = light_sensor.LightSensor()

        logging.info('Display:init')

        self.display.begin()
        self.display.set_colon(True)

    def update_display(self, time_string):
        """ Update the LCD display
        """
        self.display.print_number_str(time_string)

        # Normalise light level from sensor to an integer between 0 and 15
        light_level = int(self.sensor.get_light_level())
        if light_level > 15:
            light_level = 15

        self.display.set_brightness(light_level)
        self.display.write_display()
