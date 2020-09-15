#!/usr/bin/env python3
import Adafruit_BBIO.GPIO as GPIO
import math

SW = ["P9_26", "P9_30", "P9_41", "P9_42"] # define switches by their header pin
# Set up GPIO pins
for i in range(0, 4):
    GPIO.setup(SW[i], GPIO.IN)


def main():
    print("Welcome to etch a sketch!")
    print("")
    print("---- BUTTON LAYOUT ----")
    print("Leftmost = dimension - 1")
    print("Left middle = dimension + 1")
    print("Rightmost = confirm dimension\n")
    print("Enter x dimensions of grid below:")

    xdim = 0
    confirm = 0
    while (confirm == 0):
        if (GPIO.input(SW[1]) == 1) & (xdim < 99):      # leftmost button = decrement dimension
            xdim = xdim+1
            GPIO.wait_for_edge(SW[1], GPIO.FALLING)
        elif (GPIO.input(SW[0]) == 1) & (xdim > 0):     # middle left button = increment dimension
            xdim = xdim-1
            GPIO.wait_for_edge(SW[0], GPIO.FALLING)
        if (GPIO.input(SW[3]) == 1):                    # rightmost button = confirm
            confirm = 1
            GPIO.wait_for_edge(SW[3], GPIO.FALLING)
        print(xdim, " ", end='\r')
    print(xdim)
    
    print("Enter y dimensions of grid below:")
    ydim = 0
    confirm = 0
    while (confirm == 0):
        if (GPIO.input(SW[1]) == 1) & (ydim < 99):
            ydim = ydim+1
            GPIO.wait_for_edge(SW[1], GPIO.FALLING)
        elif (GPIO.input(SW[0]) == 1) & (ydim > 0):
            ydim = ydim-1
            GPIO.wait_for_edge(SW[0], GPIO.FALLING)
        if (GPIO.input(SW[3]) == 1):
            confirm = 1
            GPIO.wait_for_edge(SW[3], GPIO.FALLING)
        print(ydim, " ", end='\r')
    print(ydim)

    print("Preparing a(n) ", xdim, "x", ydim, "etch a sketch grid")
    xpoint = int((xdim+1)/2-1)                                           # use "ceiling" function to start drawing in center of sketch
    ypoint = int((ydim+1)/2-1)
    coordinates = [0] * xdim
    for x in range(0, xdim):                                        # create coordinates (currently matrix of zeros)
        coordinates[x] = [0] * ydim                                 # when pointer moves, change entry to 1. 
                                                                    # whenever there's a 1, place an x in the sketch; otherwise place a space
    coordinates[xpoint][ypoint] = 1
    
    newsketch(xdim, ydim, coordinates)                              # generates sketch with "x" in the center
    
    
    while True:                                                     # loop 
        print("Use leftmost, left middle, right middle, or rightmost buttons to draw left, up, down, or right")
        print("Use wa, sa, sd, or wd to draw diagonals")
        print("Type 'clear' to erase the sketch")
    
        switchmapping = ["a", "w", "s", "d"]
        direction = ""
        while (direction == ""):
            for i in range(0, 4):
                if GPIO.input(SW[i]) == 1:
                    direction = switchmapping[i]
                    GPIO.wait_for_edge(SW[i], GPIO.FALLING)
                    i = 4
                
        
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
                if str(direction[l]) == "s":                        # if cursor gets to edge of sketch, it cannot go any further
                    if ypoint == (ydim - 1):                        # (i.e. it will not wrap around the sketch to the other side)
                        ypoint = ydim - 1
                    else:
                        ypoint+=1
                elif str(direction[l]) == "a":
                    if xpoint == 0:
                        xpoint = 0
                    else:
                        xpoint-=1
                elif str(direction[l]) == "w":
                    if ypoint == 0:
                        ypoint = 0
                    else:
                        ypoint -=1
                elif str(direction[l]) == "d":
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
                etchasketch(xdim, ydim, coordinates)                    # draw the updated sketc
            if valid == 0:
                xpoint = originalxpoint
                ypoint = originalypoint
            
        
def newsketch(xdim, ydim, coordinates):
    
    line = ""
    print("  ", end =" ")
    for x in range(0, xdim):            # print out numbers along x-axis (top)
        if x < 10:
            print(x, " ", end =" ")
        elif x >= 10:
            print(x, "", end =" ")
    print("")
            
    for y in range(0, ydim):            # print out numbers along y-axis (left)
        if y < 10:
            print("", y, end =" ")
        elif y >= 10:
            print(y,)
        for x in range(0, xdim):        # place "x" in the center of the sketch
            if coordinates[x][y] == 0:
                line = line + "    "
            elif coordinates[x][y] == 1:
                line = line + "x   "
        
        print(line)
        line = ""
    

def etchasketch(xdim, ydim, coordinates):
    
    line = ""
    print("  ", end =" ")
    for x in range(0, xdim):            # print out numbers along x-axis (top)
        if x < 10:
            print(x, " ", end =" ")
        elif x >= 10:
            print(x, "", end =" ")
    print("")
    
    for y in range(0, ydim):            # print out numbers along y-axis (left)
        if y < 10:
            print("", y, end =" ")
        elif y >= 10:
            print(y, end =" ")
            
        for x in range(0, xdim):        # for each line, search through coordinates matrix
            if coordinates[x][y] == 0:  # if 0, place a space; if 1, place an "x"
                line = line + "    "
            elif coordinates[x][y] == 1:
                line = line + "x   "
        
        print(line)                      # display line, then reset and repeat for the remaining lines
        line = ""


while True:
    main()
    
