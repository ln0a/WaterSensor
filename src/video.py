#!/usr/bin/env python

import time
import vlc

def play(source):
    vlc_instance = vlc.Instance()
    player = vlc_instance.media_player_new()
    media = vlc_instance.media_new(source)
    player.set_media(media)
    player.play()
    
def play_wait_close(source):
    play(source)

    time.sleep(1.5)
    duration = player.get_length() / 1000
    time.sleep(duration)

    print("Video finished")
    # play_blank()

def play_blank():
    play("videos/block.mp4")