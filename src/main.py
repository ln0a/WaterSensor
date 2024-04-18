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
GPIO.setmode(GPIO.BCM)

# Initialise RFID reader
reader = SimpleMFRC522()

# Initialise control objects
serial = SerialController()
rfid = rfid.RFID()
video = Video()
switch = 17
GPIO.setup(switch, GPIO.IN)

initial_loop = True

if (GPIO.input(switch)):
    print("1")
elif (not GPIO.input(switch)):
    print("0")

# Sensor reading loop
try:
    while True:
        serial.ser.write(b'0')

        os.popen("killall vlc")
        time.sleep(2)
        os.popen("cvlc --repeat --fullscreen /home/e/WaterSensor/videos/hold.mp4")

        # Reset tag read toggle
        tag_read = False

        while tag_read == False:
            id = rfid.read(reader)

            if (id != rfid.previous_tag):
                if initial_loop:
                    initial_loop = False
                else:
                    tag_timer.cancel()

                rfid.previous_tag = id

                serial.ser.write(b'1')

                os.popen("killall vlc")
                time.sleep(2)
                os.popen("cvlc --fullscreen /home/e/WaterSensor/videos/" + video.files[id][0] + ".mp4")

                time.sleep(video.files[id][1] - 32)
                serial.ser.write(b'2')
                time.sleep(32)

                # Start timer thread to clear previous tag after 30s
                tag_timer = Timer(30, rfid.clear_tag)
                tag_timer.start()

                tag_read == True
            
                break


except KeyboardInterrupt:
    GPIO.cleanup()


finally:
    GPIO.cleanup()
