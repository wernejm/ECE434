#!/usr/bin/env python3
# Written by James Werne. Reads switches and lights a corresponding LED (using interrupts)

import Adafruit_BBIO.GPIO as GPIO
import time

SW = ["P9_26", "P9_30", "P9_41", "P9_42"] # define switches by their header pin
LED = ["P9_11", "P9_12", "P9_13", "P9_14"] # define LEDs by their header pin

# Set up GPIO pins
for i in range(0, 4):
    GPIO.setup(SW[i], GPIO.IN)
    GPIO.setup(LED[i], GPIO.OUT)

# define map between pushbuttons and LEDs
map = {SW[0]: LED[0], SW[1]: LED[1], SW[2]: LED[2], SW[3]: LED[3]}

# when interrupt/event occurs, callback to this function and set the LED to the value of the pushbutton
#   (i.e. if switch 1 is pushed, state = 1, so we output 1 to LED 1)
def updateLED(channel):
    state = GPIO.input(channel)
    GPIO.output(map[channel], state)
    print(map[channel] + " Toggled")

# set up interrupt on both rising and falling edge of the incoming pushbutton signals
for i in range(0, 4):
    GPIO.add_event_detect(SW[i], GPIO.BOTH, callback=updateLED)

# wait until an interrupt to occur
try:
    while True:
        time.sleep(100)

except KeyboardInterrupt:
    GPIO.cleanup()
GPIO.cleanup()
    