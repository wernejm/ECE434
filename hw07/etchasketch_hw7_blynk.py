#!/usr/bin/env python3

# James Werne
# Etch-a-Sketch for hw07
# Controlled by buttons on a blynk module

import blynklib
import os
import Adafruit_BBIO.GPIO as GPIO
import math
import smbus
import time


switchmapping = ["a", "w", "s", "d"]
direction = ""

# Get the autherization code (See setup.sh)
BLYNK_AUTH ='rYgNKhI4DNc0SlWErt4cVjsWCgmwI3nM'

# Initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH)


        

bus = smbus.SMBus(2)        # select i2c bus 2
matrix = 0x70               # define matrix address on i2c bus


# --------------------MATRIX SETUP--------------------
bus.write_byte_data(matrix, 0x21, 0)   # Start oscillator (p10)
bus.write_byte_data(matrix, 0x81, 0)   # Disp on, blink off (p11)
bus.write_byte_data(matrix, 0xe7, 0)   # Full brightness (page 15)





print("Welcome to etch a sketch!")
print("")
print("8x8 LED edition")

xdim = 8
ydim = 8

print("Preparing an ", xdim, "x", ydim, "etch a sketch grid")
xpoint = int((xdim+1)/2-1)                                           # use "ceiling" function to start drawing in center of sketch
ypoint = int((ydim+1)/2-1)
coordinates = [0] * xdim
for x in range(0, xdim):                                        # create coordinates (currently matrix of zeros)
    coordinates[x] = [0] * ydim                                 # when pointer moves, change entry to 1. 
                                                                # whenever there's a 1, place an x in the sketch; otherwise place a space
coordinates[xpoint][ypoint] = 1

grid = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x08, 0x00,         # create grid of all zeros
              0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
bus.write_i2c_block_data(matrix, 0, grid)                       # write zeros to each LED (i.e. all LEDs off)



# Register Virtual Pins
# The V* says to response to all virtual pins
@blynk.handle_event('write V*')         # if virtual button is pressed, update led matrix accordingly
def my_write_handler(pin, value):
    global direction
    global switchmapping
    global xdim
    global ydim
    global coordinates
    global grid
    
    print('Current V{} value: {}'.format(pin, value))
    if value[0] == "1":                             # if virtual button is pressed, update led matrix
        if pin == 2:                                # top button = up
            direction = switchmapping[2]
        elif pin == 3:                              # left button = left
            direction = switchmapping[0]
        elif pin == 4:                              # right button = right
            direction = switchmapping[3]
        elif pin == 5:                              # bottom button = down
            direction = switchmapping[1]
        setpoint()                                  # update matrix


	

def clear():                    # resets coordinates & clears grid
    global grid
    global xpoint
    global ypoint
    global xdim
    global ydim
    global coordinates
    
    xpoint = int((xdim+1)/2-1)                                           # use "ceiling" function to start drawing in center of sketch
    ypoint = int((ydim+1)/2-1)
    coordinates = [0] * xdim
    for x in range(0, xdim):                                        # create coordinates (currently matrix of zeros)
        coordinates[x] = [0] * ydim                                 # when pointer moves, change entry to 1. 
                                                                    # whenever there's a 1, place an x in the sketch; otherwise place a space
    coordinates[xpoint][ypoint] = 1
    
    grid = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x08, 0x00,         # create grid of all zeros
                  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
    bus.write_i2c_block_data(matrix, 0, grid)                       # write zeros to each LED (i.e. all LEDs off)
    


def etchasketch(xdim, ydim, coordinates, grid):
    
    column = 2
    onbit = 1
    dot = 0
    
    
    for y in range(0, ydim):            
        
        for x in range(0, xdim):        # for each line, search through coordinates matrix
            if coordinates[x][y] == 1:  # if 0, place a space; if 1, turn LED on
                column = 2 
                column = column*x       # select even columns (i.e. the columns controlling the green LEDs -- not the red LEDs)
                dot = grid[column]      # select the value of the matrix corresponding to the appropriate column's LED pattern
                onbit = 1<<y            # bit shift to the correct LED within the column
                grid[column] = onbit | dot      # set that LED on
                
        
    bus.write_i2c_block_data(matrix, 0, grid)   # after updating grid matrix, turn on appropriate LEDs




def setpoint():                         # used to set the coordinate based on button input from the flask web browser
    
    global xpoint
    global ypoint
    global direction
    global grid
    

    originalxpoint = xpoint
    originalypoint = ypoint
    valid = 1
    if direction == "w":                        # if cursor gets to edge of sketch, it cannot go any further
        if ypoint == (ydim - 1):                        # (i.e. it will not wrap around the sketch to the other side)
            ypoint = ydim - 1
        else:
            ypoint+=1
    elif direction == "d":
        if xpoint == 0:
            xpoint = 0
        else:
            xpoint-=1
    elif direction == "s":
        if ypoint == 0:
            ypoint = 0
        else:
            ypoint -=1
    elif direction == "a":
        if xpoint == (xdim - 1):
            xpoint = xdim - 1
        else:
            xpoint +=1
    else:
        print("Please enter a valid direction")          # if any character other than wasd is entered, throw a warning
        valid = 0
        xpoint = originalxpoint
        ypoint = originalypoint
    
    if valid == 1:    
        coordinates[xpoint][ypoint] = 1                         # change entry in coordinates matrix based on where the pointer is
        etchasketch(xdim, ydim, coordinates, grid)                    # draw the updated sketch
    if valid == 0:
        xpoint = originalxpoint
        ypoint = originalypoint


clear()

while True:
    blynk.run()
