#!/usr/bin/env python

import time
import board
import neopixel

led_quantity = 24
pixels = neopixel.NeoPixel(board.D18, led_quantity,
                           brightness=0.1, auto_write=False)


def fill_in(pause):
    for i in range(led_quantity):
        pixels[i] = (0, 0, 0)
        time.sleep(pause)


def fill(r, g, b):
    pixels.fill((r, g, b))


def rotate(r, g, b, pause):
    i = 0
    size = 4

    while True:
        fill(0, 0, 0)

        for j in range(size):
            num_list = group(i, led_quantity, size)
            pixels[num_list[j]] = (r, g, b)

        if i < led_quantity - 1:
            i += 1
        else:
            i = 0

        time.sleep(pause)
        pixels.show()


# Returns array of positions based on specific position and quantity
def group(position, max, group_size):
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
