#!/usr/bin/env python

import time
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import rfid

# Hide all GPIO warnings
GPIO.setwarnings(False)

# Initialise RFID reader
reader = SimpleMFRC522()


# Sensor reading loop
try:
    while True:
        rfid.read(reader)
        time.sleep(2)
except KeyboardInterrupt:
    GPIO.cleanup()
finally:
    GPIO.cleanup()
