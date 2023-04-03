#!/usr/bin/env python

import threading
import video
import led

# Water sample RFID tag labels
sample_tags = {
    632153281131: 'videos/algae.mp4', 
    975930237824: 'videos/clean.mp4', 
    842353281731: 'videos/pollution.mp4'}

# Read RFID tag and lookup tags
def read(reader):
    id, label = reader.read()
    lookup_rfid_tag(id)

# Check if tag id is stored in tag dictionary
# and play associated video file
def lookup_rfid_tag(id):
    if id in sample_tags:
        # print(sample_tags[id])
        t1 = threading.Thread(target=led.rotate, args=(0, 0, 255, 0.03,))
        t2 = threading.Thread(target=video.play_wait_close, args=(sample_tags[id],))

        t1.start()
        t2.start()

        t1.join()
        t2.join()
    else:
        print('No tag found')