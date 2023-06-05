#!/usr/bin/env python

import time
import threading
import video
import led


# Water sample RFID tag labels
sample_tags = {
    632153281131: "videos/Sewage.mp4",
    975930237824: "videos/Flooding.mp4",
    842353281731: "videos/Pollution.mp4"}


class RFID(object):

    # Read RFID tag and lookup tags
    def read(self, reader):
        id, label = reader.read()

        if self.lookup_rfid_tag(id):
            self.print_tag(id)
            return sample_tags[id]

    # Check if tag id is stored in tag dictionary
    # and play associated video file
    def lookup_rfid_tag(self, tag):
        if tag in sample_tags:
            return True

    def print_tag(self, id):
        print("")
        print("RFID tag " + str(id) + ": playing " + sample_tags[id])