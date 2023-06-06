#!/usr/bin/env python

import time
import os
from threading import Thread, Timer
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import rfid
from video import Video
from led import LED


# Hide all GPIO warnings
GPIO.setwarnings(False)

# Initialise RFID reader
reader = SimpleMFRC522()

# Initialise control objects
rfid = rfid.RFID()
led = LED()
video = Video()

thread_led = Thread(target=led.rotate)
thread_led.start()


# Sensor reading loop
try:
    while True:
        os.popen("killall vlc")
        time.sleep(2)
        os.popen("cvlc --loop --fullscreen /home/e/WaterSensor/videos/hold.mp4")

        if rfid.read(reader):
            led.speed_change(0.02)
            led.color_change((0, 255, 0))

            id = rfid.read(reader)

            os.popen("killall vlc")
            time.sleep(2)
            os.popen("cvlc --fullscreen /home/e/WaterSensor/videos/" + video.files[id] + ".mp4")

            time.sleep(20)
            
            led.speed_reset()
            led.color_reset()


except KeyboardInterrupt:
    thread_led.join()
    GPIO.cleanup()

finally:
    thread_led.join()
    GPIO.cleanup()
