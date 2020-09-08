#!/usr/bin/env python
import math


def main():
    print "Welcome to etch a sketch!"
    print ""
    print "Enter x dimensions of grid below:" 

    xdim = ""
    while (xdim == ""):
        xdim = input()                                              # wait for user input
        if xdim > 99:
            xdim = ""
            print "Please enter a number less than 100"
        
    print "Enter y dimensions of grid below:"
    ydim = ""
    while (ydim == ""):
        ydim = input()                                              # wait for user input
        if ydim > 99:
            ydim = ""
            print "Please enter a number less than 100"

    print "Preparing a(n) ", xdim, "x", ydim, "etch a sketch grid"
    xpoint = (xdim+1)/2-1                                           # use "ceiling" function to start drawing in center of sketch
    ypoint = (ydim+1)/2-1
    coordinates = [0] * xdim
    for x in range(0, xdim):                                        # create coordinates (currently matrix of zeros)
        coordinates[x] = [0] * ydim                                 # when pointer moves, change entry to 1. 
                                                                    # whenever there's a 1, place an x in the sketch; otherwise place a space
    coordinates[xpoint][ypoint] = 1
    
    newsketch(xdim, ydim, coordinates)                              # generates sketch with "x" in the center
    
    
    while True:                                                     # loop 
        print "Use w, a, s, d to draw up, down, left, or right"
        print "Use wa, sa, sd, or wd to draw diagonals"
        print "Type 'clear' to erase the sketch"
        direction = ""
        while (direction == ""):
            direction = raw_input()
        
        if len(direction) > 2:                                      # if "clear" is typed, erase sketch & reset if 
            if direction == "clear":
                print "Erasing sketch"
                print ""
                print ""
                break
            else:
                print "Please enter a valid direction"              # if more than two characters are entered (other than "clear"), throw a warning
        elif (direction == "ss") | (direction == "ww") | (direction == "aa") | (direction == "dd"):
            print "Please enter a valid direction"                  # if ww, aa, ss, or dd is entered, throw a warning
        else:
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
                    print "Please enter a valid direction"          # if any character other than wasd is entered, throw a warning
                
            coordinates[xpoint][ypoint] = 1                         # change entry in coordinates matrix based on where the pointer is
                
            etchasketch(xdim, ydim, coordinates)                    # draw the updated sketch
                    
                
            
        
def newsketch(xdim, ydim, coordinates):
    
    line = ""
    print "  ",
    for x in range(0, xdim):            # print out numbers along x-axis (top)
        if x < 10:
            print x, " ",
        elif x >= 10:
            print x, "",
    print ""
            
    for y in range(0, ydim):            # print out numbers along y-axis (left)
        if y < 10:
            print "", y,
        elif y >= 10:
            print y,
        for x in range(0, xdim):        # place "x" in the center of the sketch
            if coordinates[x][y] == 0:
                line = line + "    "
            elif coordinates[x][y] == 1:
                line = line + "x   "
        
        print line
        line = ""
    

def etchasketch(xdim, ydim, coordinates):
    
    line = ""
    print "  ",
    for x in range(0, xdim):            # print out numbers along x-axis (top)
        if x < 10:
            print x, " ",
        elif x >= 10:
            print x, "",
    print ""
    
    for y in range(0, ydim):            # print out numbers along y-axis (left)
        if y < 10:
            print "", y,
        elif y >= 10:
            print y,
            
        for x in range(0, xdim):        # for each line, search through coordinates matrix
            if coordinates[x][y] == 0:  # if 0, place a space; if 1, place an "x"
                line = line + "    "
            elif coordinates[x][y] == 1:
                line = line + "x   "
        
        print line                      # display line, then reset and repeat for the remaining lines
        line = ""


while True:
    main()
    
