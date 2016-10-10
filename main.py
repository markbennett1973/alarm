import display
import alarm
import button
import timer
import time
import google_api

my_api = google_api.GoogleApi()
my_display = display.Display()
my_alarm = alarm.Alarm(my_api)
my_button = button.Button(my_alarm, my_display)
my_timer = timer.Timer(my_display, my_alarm, my_button)

while True:
    time.sleep(1)