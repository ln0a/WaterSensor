#!/usr/bin/env python

import time
import threading
import video
import led


# Water sample RFID tag labels
sample_tags = {
    632153281131: 'videos/algae.mp4',
    975930237824: 'videos/clean.mp4',
    842353281731: 'videos/pollution.mp4'}


class RFID(object):

    # Read RFID tag and lookup tags
    def read(self, reader, player, led):
        id, label = reader.read()

        if self.lookup_rfid_tag(id):
            self.print_tag(id)

            led.speed_change(0.03)
            led.color_change((0, 255, 0))

            player.addVideo(sample_tags[id])
            player.play()
            player.wait_stop()

            led.speed_reset()
            led.color_reset()

    # Check if tag id is stored in tag dictionary
    # and play associated video file
    def lookup_rfid_tag(self, tag):
        if tag in sample_tags:
            return True
        else:
            print('No tag found')
            return False

    def print_tag(self, id):
        print("")
        print("RFID tag " + str(id) + ": playing " + sample_tags[id])