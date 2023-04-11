#!/usr/bin/env python

import time
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import rfid
import threading
import video
import led


# Hide all GPIO warnings
GPIO.setwarnings(False)

# Initialise RFID reader
reader = SimpleMFRC522()

# Initialise video player
player = video.VLC()

# Sensor reading loop
try:
    while True:
        # t1 = threading.Thread(target=led.rotate, args=(0, 0, 255, 0.1,))
        # t2 = threading.Thread(target=rfid.read, args=(reader,))

        # t1.start()
        # t2.start()

        # t1.join()
        # t2.join()

        player.addVideo("videos/pollution.mp4")
        player.play()

        rfid.read(reader, player)

except KeyboardInterrupt:
    GPIO.cleanup()

finally:
    GPIO.cleanup()
