#!/usr/bin/env python

import time
import vlc


class VLC(object):

    def __init__(self):
        self.Instance = vlc.Instance()
        self.Player = self.Instance.media_player_new()
        self.Player.set_fullscreen(True)

    def addVideo(self, source):
        self.Media = self.Instance.media_new(source)
        self.Player.set_media(self.Media)

    def play(self):
        self.Player.play()

    def wait(self):
        time.sleep(2)
        duration = self.Player.get_length() / 1000
        time.sleep(duration)

    def wait_stop(self):
        self.wait()
        self.Player.stop()

    def loop(self):
        self.play()
        self.wait_stop()
        self.loop()

    def stop(self):
        self.Player.stop()