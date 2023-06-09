#!/usr/bin/env python

import time
import os
from threading import Thread, Timer
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from serial_controller import SerialController
import rfid
from video import Video


# Hide all GPIO warnings
GPIO.setwarnings(False)

# Initialise RFID reader
reader = SimpleMFRC522()

# Initialise control objects
serial = SerialController()
rfid = rfid.RFID()
video = Video()


# Sensor reading loop
try:
    while True:
        serial.ser.write(b'0')

        os.popen("killall vlc")
        time.sleep(2)
        os.popen("cvlc --repeat --fullscreen /home/e/WaterSensor/videos/hold.mp4")

        if rfid.read(reader):
            serial.ser.write(b'1')

            id = rfid.read(reader)

            os.popen("killall vlc")
            time.sleep(2)
            os.popen("cvlc --fullscreen /home/e/WaterSensor/videos/" + video.files[id][0] + ".mp4")

            time.sleep(video.files[id][1] - 32)
            serial.ser.write(b'2')
            time.sleep(32)


except KeyboardInterrupt:
    GPIO.cleanup()


finally:
    GPIO.cleanup()
