#!/bin/sh

# Set the sound volume level
amixer set PCM -- 1000

cd /home/pi/alarm
python main.py