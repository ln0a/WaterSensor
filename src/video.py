#!/usr/bin/env python

import time
import os


class Video(object):

    def __init__(self):
        self.files = {
            584192178468: ["flooding", 299],
            584191785278: ["pollution", 283],
            584191392048: ["sewage", 295],
        }

    def hold_play(self, serial):
        serial.ser.write(b'0')

        os.popen("killall vlc")
        time.sleep(2)
        os.popen("cvlc --fullscreen /home/e/WaterSensor/videos/hold.mp4")

        time.sleep(20)

    def video_play(self, id, serial):
        serial.ser.write(b'1')

        os.popen("killall vlc")
        time.sleep(2)
        os.popen("cvlc --fullscreen /home/e/WaterSensor/videos/" + self.files[id][0] + ".mp4")

        time.sleep(self.files[id][1] - 32)
        serial.ser.write(b'2')
        time.sleep(32)