#!/usr/bin/env python3

# James Werne
# Etch-a-Sketch for hw03
# Controlled by rotary encoders & displays grid on LED matrix

from Adafruit_BBIO.Encoder import RotaryEncoder, eQEP2, eQEP1
import math
import smbus
import time

bus = smbus.SMBus(2)        # select i2c bus 2
matrix = 0x70               # define matrix address on i2c bus


# --------------------MATRIX SETUP--------------------
bus.write_byte_data(matrix, 0x21, 0)   # Start oscillator (p10)
bus.write_byte_data(matrix, 0x81, 0)   # Disp on, blink off (p11)
bus.write_byte_data(matrix, 0xe7, 0)   # Full brightness (page 15)


SW = ["P8_11", "P8_12", "P8_33", "P8_35"] # define switches by their header pin

# set up left/right rotary encoder & refresh at 1000kHz
lrEncoder = RotaryEncoder(eQEP2)
lrEncoder.zero()
lrEncoder.setAbsolute()
lrEncoder.frequency = 1000
lrEncoder.enable()
# set up up/down rotary encoder
udEncoder = RotaryEncoder(eQEP1)
udEncoder.zero()
udEncoder.setAbsolute()
udEncoder.frequency = 1000
udEncoder.enable()


def main():
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

    
    while True:                                                     # loop 
        print("Use left rotary encoder to draw left/right, and use right encoder to draw up/down")
        
        lrEncoder.zero()
        udEncoder.zero()                        # zero the encoders
        
        switchmapping = ["a", "w", "s", "d"]
        direction = ""
        while (direction == ""):
            if lrEncoder.position > 0:          # if encoder is turned CCW, draw left
                direction = switchmapping[0]
            elif lrEncoder.position < 0:
                direction = switchmapping[3]    # if encoder is turned CW, draw right
            elif udEncoder.position > 0:
                direction = switchmapping[1]    # if encoder is turned CW, draw up
            elif udEncoder.position < 0:
                direction = switchmapping[2]    # if encoder is turned CCW, draw down
            
            time.sleep(0.1)

                
        
        if len(direction) > 2:                                      # if "clear" is typed, erase sketch & reset if 
            if direction == "clear":
                print("Erasing sketch")
                print("")
                print("")
                break
            else:
                print("Please enter a valid direction")              # if more than two characters are entered (other than "clear"), throw a warning
        elif (direction == "ss") | (direction == "ww") | (direction == "aa") | (direction == "dd"):
            print("Please enter a valid direction")                  # if ww, aa, ss, or dd is entered, throw a warning
        else:
            originalxpoint = xpoint
            originalypoint = ypoint
            valid = 1
            for l in range(0, len(direction)):
                if str(direction[l]) == "w":                        # if cursor gets to edge of sketch, it cannot go any further
                    if ypoint == (ydim - 1):                        # (i.e. it will not wrap around the sketch to the other side)
                        ypoint = ydim - 1
                    else:
                        ypoint+=1
                elif str(direction[l]) == "d":
                    if xpoint == 0:
                        xpoint = 0
                    else:
                        xpoint-=1
                elif str(direction[l]) == "s":
                    if ypoint == 0:
                        ypoint = 0
                    else:
                        ypoint -=1
                elif str(direction[l]) == "a":
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
                etchasketch(xdim, ydim, coordinates, grid)                    # draw the updated sketc
            if valid == 0:
                xpoint = originalxpoint
                ypoint = originalypoint
            
    

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
        


while True:
    main()


