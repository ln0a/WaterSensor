#!/usr/bin/env python

import time
import threading


# Water sample RFID tag labels
# sample_tags = {
#     632153281131: "flooding",
#     975930237824: "pollution",
#     842353281731: ""}
sample_tags = {
    584191392048: ["sewage", 295],
    584191785278: ["pollution", 295],
    584192178468: ["flooding", 295]
}


class RFID(object):

    # Read RFID tag and lookup tags
    def read(self, reader):
        id, label = reader.read()

        if self.lookup_rfid_tag(id):
            # self.print_tag(id)
            # return sample_tags[id]
            clean_label = "".join(label.split())
            print("label: " + clean_label + ".")
            # return clean_label
            return id

    # Check if tag id is stored in tag dictionary
    # and play associated video file
    def lookup_rfid_tag(self, tag):
        if tag in sample_tags:
            return True

    def print_tag(self, id):
        print("")
        print("RFID tag " + str(id) + ": playing " + sample_tags[id])