#!/bin/sh
# TempRead.sh
# Written by James Werne
# Reads temperature sensors, converts to degrees Fahrenheit,
#	and outputs that temperature


config-pin P9_19 i2c
config-pin P9_20 i2c

temp=$(i2cget -y 2 0x48) 	# measure temp on left sensor
templ=$(($temp *9/5 +32))	# convert to Fahrenheit
temp=$(i2cget -y 2 0x4a)	# measure right sensor
tempr=$(($temp *9/5 +32))
echo "The temperature of the left sensor is: " $templ
echo "The temperature of the right sensor is: " $tempr

