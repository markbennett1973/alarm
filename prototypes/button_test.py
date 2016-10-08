import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    if GPIO.input(15):
        GPIO.output(14, GPIO.LOW)
    else:
        GPIO.output(14, GPIO.HIGH)
    time.sleep(0.1)