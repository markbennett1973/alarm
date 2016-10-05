import display
import alarm
import button
import timer
import time

my_display = display.Display()
my_alarm = alarm.Alarm()
my_button = button.Button(my_alarm, my_display)
my_timer = timer.Timer(my_display, my_alarm)

while True:
    time.sleep(1)