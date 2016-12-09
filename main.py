import display
import alarm
import button
import timer
import google_api
import logging
from flask import Flask
from web import routes


logging.basicConfig(format='%(asctime)s %(message)s', filename='alarm.log', level=logging.INFO)

""" Initialise the alarm clock objects
"""
my_api = google_api.GoogleApi()
my_display = display.Display()
my_alarm = alarm.Alarm(my_api)
my_button = button.Button(my_alarm, my_display)
my_timer = timer.Timer(my_display, my_alarm, my_button)

app = Flask(__name__)
app.register_blueprint(routes)

app.run(host='0.0.0.0', port=80)
