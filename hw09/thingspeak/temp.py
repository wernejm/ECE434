#!/usr/bin/env python3
# Reads a TMP101 sensor and posts its temp on ThinkSpeak
# https://thingspeak.com/channels/538706
# source setup.sh to set THING_KEY

# Edited by James Werne, 11/4/2020
# Reads values of TMP101 sensors, then prints them to a Thingspeak channel:
# https://thingspeak.com/channels/1220211/private_show

import requests
import os, sys
import time
import smbus
import time

bus = smbus.SMBus(2)
TMPleft = 0x48
TMPright = 0x4a


#TMP101a='/sys/class/i2c-adapter/i2c-2/2-0048/hwmon/hwmon0/'
#TMP101b='/sys/class/i2c-adapter/i2c-2/2-0049/hwmon/hwmon1/'

# Get the key (See setup.sh)
key = os.getenv('THING_KEY', default="")
if(key == ""):
    print("THING_KEY is not set")
    sys.exit()

url = 'https://api.thingspeak.com/update'
print(url)

templ = bus.read_byte_data(TMPleft, 0)      # Read temp
templ = round(templ*1.8 + 32, 1)            # convert to Fahrenheit & round to nearest tenths place
tempr = bus.read_byte_data(TMPright, 0)
tempr = round(tempr*1.8 + 32, 1)

# f = open(TMP101a+'temp1_input', "r")
# temp1=f.read()[:-1]     # Remove trailing new line
# # Convert from mC to C
# temp1 = int(temp1)/1000
# f.close()
# print("temp1: " + str(temp1))

# f = open(TMP101b+'temp1_input', "r")
# temp2=f.read()[:-1]
# temp2 = int(temp2)/1000
# f.close()
# print("temp2: " + str(temp2))

payload = dict(api_key=key, field1=templ, field2=tempr)
r = requests.get(url, stream=True, data=payload)
# print(r)
# print(r.text)

# time.sleep(15*60)
