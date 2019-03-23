# Alarm Pi

Code to run an alarm clock on a Raspberry Pi

## Installation

burn new raspbian image to sd card
enable headless wifi and ssh config

get alarm repo

sudo apt-get update
sudo apt-get install build-essential python-dev
sudo apt-get install python-smbus python-pip python-pygame libsdl1.2-dev python-rpi.gpio python-dateutil

Get LED backpack library: https://github.com/adafruit/Adafruit_Python_LED_Backpack

From led backpack directory;
sudo python setup.py install

Get GPIO libarary: https://github.com/adafruit/Adafruit_Python_GPIO

From GPIO directory;
sudo python setup.py install

enable i2c using sudo raspi-config (under interfacing options)

sudo python -m pip install -U pytz
sudo python -m pip install -U httplib2
sudo python -m pip install -U google-api-python-client
sudo python -m pip install -U oauth2client
sudo apt-get install python-dateutil
sudo python -m pip install -U flask

To start alarm clock on boot, add to /etc/rc.local:
sudo python /home/pi/alarm/main.py &

On a desktop machine, run google_auth.py to generate google auth token, and save to google-credentials.json in alarm directory