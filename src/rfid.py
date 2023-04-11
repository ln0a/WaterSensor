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


# Read RFID tag and lookup tags
def read(reader, player):
    id, label = reader.read()

    if lookup_rfid_tag(id):
        player.addVideo(sample_tags[id])
        player.play()
        player.wait_stop()


# Check if tag id is stored in tag dictionary
# and play associated video file
def lookup_rfid_tag(id):
    if id in sample_tags:
        return True
    else:
        print('No tag found')
        return False
