#!/usr/bin/env python

import serial


class SerialController(object):

    def __init__(self):
        self.ser = serial.Serial("/dev/ttyUSB0", 9600)
        self.ser.flushInput()

    def write(self, message):
        if (self.ser.is_open()):
            print("Serial open")
            print("Message: " + message)
            self.ser.write(b'')