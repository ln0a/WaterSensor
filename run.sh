#! /usr/bin/env bash

unclutter -idle 0.1 -root & (sxiv -a image/loop-infinite.gif -fb -z 400 & sudo python3 src/main.py)