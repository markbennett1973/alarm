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
        if len(time_string) < 4:
            time_string = '    ' + time_string
            time_string = time_string[-4:]

        self.display.print_number_str(time_string)

        # Normalise light level from sensor to an integer between 0 and 15
        light_level = self.normalise_light_level(int(self.sensor.get_light_level()))
        logging.debug('Display: update brightness to ' + str(light_level))

        self.display.set_brightness(light_level)
        self.display.write_display()

    def normalise_light_level(self, level):
        if level < 0.05:
            return 0
        elif level < 0.1:
            return 5
        elif level < 0.2:
            return 10
        else:
            return 15
