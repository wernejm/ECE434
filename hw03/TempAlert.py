#!/usr/bin/env python3
# Written by James Werne. Sets the temperature limits for both sensors,
#   then waits for an interrupt on the ALERT pin & prints the temperature in F.

import smbus
import Adafruit_BBIO.GPIO as GPIO
import time

bus = smbus.SMBus(2)
TMPleft = 0x48                      # TMP101 left sensor has address of 1001 000
TMPright = 0x4a                     # TMP101 right sensor has address of 1001 010
TMPleftalert = "P9_23"
TMPrightalert = "P9_27"
GPIO.setup(TMPleftalert, GPIO.IN)   # set alert port to input
GPIO.setup(TMPrightalert, GPIO.IN)

Thigh = 25              # set high and low limits to 25 C.
Tlow = 25


bus.write_byte_data(TMPleft, 1, 0x06)       # Config register: turn on "Alert" mode (+2)
bus.write_byte_data(TMPright, 1, 0x06)      # set POL = 1 (+4), so write 4+2=6 to register
bus.write_byte_data(TMPleft, 3, Thigh)      # wrote Thigh & Tlow values to left sensor
bus.write_byte_data(TMPleft, 2, Tlow)
bus.write_byte_data(TMPright, 3, Thigh)     # wrote Thigh & Tlow values to right sensor 
bus.write_byte_data(TMPright, 2, Tlow)


def printTemp(channel):                     # interrupt function:
    if (TMPleftalert==channel):             # if left sensor is triggered, read temp, convert to F, and print
        temp = bus.read_byte_data(TMPleft, 0)
        temp = round(1.8*temp+32, 1)
        print("Left sensor alarm: temperature value is ", temp)

    if (TMPrightalert==channel):            # if right sensor is triggered, read temp, convert to F, and print
        temp = bus.read_byte_data(TMPright, 0)
        temp = round(1.8*temp+32, 1)
        print("Right sensor alarm: temperature value is ", temp)


GPIO.add_event_detect(TMPleftalert, GPIO.BOTH, callback=printTemp)      # set interrupts for left & right sensors
GPIO.add_event_detect(TMPrightalert, GPIO.BOTH, callback=printTemp)

# wait until an interrupt to occur
try:
    while True:
        time.sleep(1)
                # DEBUGGING CODE
        #print(GPIO.input(TMPleftalert))
        #print(bus.read_byte_data(TMPleft,0))
        #print(bus.read_byte_data(TMPright,0))


except KeyboardInterrupt:
    GPIO.cleanup()
GPIO.cleanup()