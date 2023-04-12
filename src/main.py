#!/usr/bin/env python

import time
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import rfid
from threading import Thread
from video import VLC
from led import LED
import vlc


# Hide all GPIO warnings
GPIO.setwarnings(False)

# Initialise RFID reader
reader = SimpleMFRC522()

# Initialise control objects
rfid = rfid.RFID()
player = VLC()
led = LED()


thread_led = Thread(target = led.rotate)
thread_led.start()

# Sensor reading loop
try:
    while True:
        player.addVideo("videos/pollution.mp4")
        player.play()

        if rfid.read(reader):
            led.speed_change(0.02)
            led.color_change((0, 255, 0))

            player.addVideo(rfid.read(reader))
            player.play()
            player.wait()

            led.speed_reset()
            led.color_reset()

except KeyboardInterrupt:
    thread_led.join()
    GPIO.cleanup()

finally:
    thread_led.join()
    GPIO.cleanup()
