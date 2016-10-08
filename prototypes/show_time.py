import time
import datetime
from Adafruit_LED_Backpack import SevenSegment
import light_sensor

display = SevenSegment.SevenSegment()
sensor = light_sensor.LightSensor()

display.begin()
display.set_colon(True)

while True:
    myTime = datetime.datetime.now().strftime("%I%M").lstrip('0')
    display.print_number_str(myTime)
    light_level = int(sensor.get_light_level())
    if light_level > 15:
        light_level = 15

    display.set_brightness(light_level)
    display.write_display()
    time.sleep(1)
