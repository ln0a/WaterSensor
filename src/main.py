#!/usr/bin/env python

from sleep import time
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


# Sensor reading loop
try:
    while True:
        t1 = threading.Thread(target=led.rotate, args=(0, 0, 255, 0.1,))
        t2 = threading.Thread(target=rfid.read, args=(reader,))

        t1.start()
        t2.start()

        t1.join()
        t2.join()

        time.sleep(2)
except KeyboardInterrupt:
    GPIO.cleanup()
finally:
    GPIO.cleanup()
