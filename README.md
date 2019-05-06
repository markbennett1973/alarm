# Alarm Pi

Code to run an alarm clock on a Raspberry Pi

## Installation

- burn new raspbian image to sd card
- enable headless wifi and ssh config
- get alarm repo
- `chmod +x alarm/launcher.sh`
- upload a suitable piece of music to `alarm.mp3`

Install python dependencies

 - sudo apt-get update
 - sudo apt-get install build-essential python-dev
 - sudo apt-get install python-smbus python-pip python-pygame libsdl1.2-dev python-rpi.gpio python-dateutil

Get LED backpack library: https://github.com/adafruit/Adafruit_Python_LED_Backpack

From led backpack directory: `sudo python setup.py install`

Get GPIO libarary: https://github.com/adafruit/Adafruit_Python_GPIO

From GPIO directory: `sudo python setup.py install`

run `sudo raspi-config`

- enable i2c (under interfacing options)
- set timezone (under localisation options)

Install more dependencies:

- sudo python -m pip install -U pytz
- sudo python -m pip install -U httplib2
- sudo python -m pip install -U google-api-python-client
- sudo python -m pip install -U oauth2client
- sudo apt-get install python-dateutil
- sudo python -m pip install -U flask

To start alarm clock on boot, add to /etc/rc.local:

`sudo /home/pi/alarm/launcher.sh &`

On a desktop machine, run google_auth.py to generate google auth token, and save to google-credentials.json in alarm directory
