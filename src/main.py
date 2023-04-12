#!/usr/bin/env python

import time
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import rfid
from threading import Thread
from video import VLC
from led import LED


# Hide all GPIO warnings
GPIO.setwarnings(False)

# Initialise RFID reader
reader = SimpleMFRC522()

# Initialise control objects
rfid = rfid.RFID()
player = VLC()
led = LED()


tread_led = Thread(target = led.rotate)
tread_led.start()


# Sensor reading loop
try:
    while True:
        player.addVideo("videos/pollution.mp4")
        player.play()

        rfid.read(reader, player, led)

except KeyboardInterrupt:
    thread_led.join()
    GPIO.cleanup()

finally:
    thread_led.join()
    GPIO.cleanup()
