#!/usr/bin/env python3
# Written by James Werne. Reads temperature of the left TMP101 sensor & outputs the value to a blynk display
#   Rounds temperature to nearest tenths place.

import blynklib
import os
import Adafruit_BBIO.GPIO as GPIO
import smbus
import time

bus = smbus.SMBus(2)
TMPleft = 0x48
TMPright = 0x4a

# Get the autherization code (See setup.sh)
#BLYNK_AUTH = os.getenv('BLYNK_AUTH')
BLYNK_AUTH='rYgNKhI4DNc0SlWErt4cVjsWCgmwI3nM'
# Initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH)



while True:
    blynk.run()
    templ = bus.read_byte_data(TMPleft, 0)      # Read temp
    templ = round(templ*1.8 + 32, 1)            # convert to Fahrenheit & round to nearest tenths place
    blynk.virtual_write(1, templ)  # Virtual display
    time.sleep(1)                   # refresh rate of virtual pin
    
    
