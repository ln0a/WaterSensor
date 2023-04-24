#!/usr/bin/env python

import time
import board
import neopixel


class LED(object):

    def __init__(self):
        self.led_quantity = 24
        self.pixels = neopixel.NeoPixel(board.D18, self.led_quantity, brightness=0.1, auto_write=False)
        self.base_speed = 0.1
        self.speed = self.base_speed
        self.base_color = (0, 0, 255)
        self.color = self.base_color

    def speed_change(self, speed):
        self.speed = speed
    def speed_reset(self):
        self.speed = self.base_speed

    def color_change(self, color):
        self.color = color
    def color_reset(self):
        self.color = self.base_color

    def blank(self):
        self.pixels.fill((0, 0, 0))

    def fill_in_timed(self, color, pause):
        for i in range(led_quantity):
            self.pixels[i] = color
            time.sleep(pause)

    def fill(self, color):
        self.pixels.fill(color)
        self.pixels.show()

    def rotate(self):
        i = 0
        size = 8

        while True:
            self.blank()

            for j in range(size):
                num_list = self.group(i, self.led_quantity, size)
                self.pixels[num_list[j]] = self.color

            if i < self.led_quantity - 1:
                i += 1
            else:
                i = 0

            time.sleep(self.speed)
            self.pixels.show()

    # Returns array of positions within a 0 - max indexed circle
    # Accepts a specific position, circle max length and group size
    def group(self, position, max, group_size):
        # Initialise empty list
        position_list = [None] * group_size

        overflow = 0

        for i in range(group_size):
            # Check if current position is lager than max length
            if position + i > max - 1:
                position_list[i] = overflow
                overflow += 1
            else:
                position_list[i] = position + i

        return position_list
