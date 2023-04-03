#!/usr/bin/env python

import video

# Water sample RFID tag labels
sample_tags = {
    632153281131: '../videos/algae.mp4', 
    975930237824: '../videos/clean.mp4', 
    842353281731: '../videos/pollution.mp4'
    }

# Read RFID tag and lookup tags
def read(reader):
    id, label = reader.read()
    lookup_rfid_tag(id)

# Check if tag id is stored in tag dictionary
# and play associated video file
def lookup_rfid_tag(id):
    if id in sample_tags:
        print(sample_tags[id])
        video.play(sample_tags[id])
    else:
        print('No tag found')