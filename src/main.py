#!/usr/bin/env python

import time
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import rfid
from threading import Thread, Timer
from video import VLC
from led import LED
import vlc
import os


# Hide all GPIO warnings
GPIO.setwarnings(False)

# Initialise RFID reader
reader = SimpleMFRC522()

# Initialise control objects
rfid = rfid.RFID()
player = VLC()
led = LED()

thread_led = Thread(target=led.rotate)
thread_led.start()

# videoPath = "cvlc ~/WaterSensor/videos/Hold.mp4"
# thread_video = Thread(target=os.popen(videoPath))
# thread_video.start()


# Sensor reading loop
try:
    while True:
        # player.addVideo("videos/Hold.mp4")
        # player.loop()
        os.popen("killall vlc")
        time.sleep(2)
        os.popen("cvlc --loop --fullscreen ~/WaterSensor/videos/Hold.mp4")

        if rfid.read(reader):
            led.speed_change(0.02)
            led.color_change((0, 255, 0))

            # player.addVideo(rfid.read(reader))
            # player.play()
            # player.wait_stop()
            os.popen("killall vlc")
            time.sleep(2)
            os.popen("cvlc --fullscreen ~/WaterSensor/videos/Flooding60.mp4")

            time.sleep(10)
            
            led.speed_reset()
            led.color_reset()


except KeyboardInterrupt:
    thread_led.join()
    GPIO.cleanup()

finally:
    thread_led.join()
    GPIO.cleanup()
