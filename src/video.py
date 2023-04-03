#!/usr/bin/env python

import vlc

def play(file):
    media = vlc.MediaPlayer(file)
    media.play()