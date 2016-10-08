from Adafruit_LED_Backpack import SevenSegment
import light_sensor


class Display:
    # Handle displaying data on the LCD screen
    display = None
    sensor = None

    def __init__(self):
        # Nothing yet - will initialise display as in light_sensor.py
        self.display = SevenSegment.SevenSegment()
        self.sensor = light_sensor.LightSensor()

        self.display.begin()
        self.display.set_colon(True)

    def update_display(self, time_string):
        # Update the display with time
        self.display.print_number_str(time_string)

        light_level = int(self.sensor.get_light_level())
        if light_level > 15:
            light_level = 15

        self.display.set_brightness(light_level)
        self.display.write_display()
