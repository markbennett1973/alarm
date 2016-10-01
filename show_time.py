import time
import datetime
from Adafruit_LED_Backpack import SevenSegment

# Create display instance on default I2C address (0x70) and bus number.
display = SevenSegment.SevenSegment()

display.begin()

# 0 - 15
display.set_brightness(8)

while True:
        display.set_colon(True)
        myTime = datetime.datetime.now().strftime("%I%M").lstrip('0')
        display.print_number_str(myTime)
        display.write_display()
        time.sleep(1)