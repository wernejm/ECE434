#!/usr/bin/env python3
# Written by James Werne. Reads temperature of two TMP101 sensors & outputs the values
#   Rounds temperature to nearest tenths place.

import smbus
import time

bus = smbus.SMBus(2)
TMPleft = 0x48
TMPright = 0x4a

while True:
    templ = bus.read_byte_data(TMPleft, 0)      # Read temp
    templ = round(templ*1.8 + 32, 1)            # convert to Fahrenheit & round to nearest tenths place
    tempr = bus.read_byte_data(TMPright, 0)
    tempr = round(tempr*1.8 + 32, 1)
    print("Left sensor temp: ", templ, " Right sensor temp: ", tempr, end="\r")     # print to terminal
    time.sleep(0.25)
    