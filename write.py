#!/usr/bin/env python

# Tag can be read at max 20mm from reader 

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
    text = input('New data: ')
    print('Now place your tag to write')
    reader.write(text)
    print('Written')
finally:
    GPIO.cleanup()