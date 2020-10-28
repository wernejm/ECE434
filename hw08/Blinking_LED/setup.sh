#!/bin/bash

export TARGET=blink_gpio31

echo TARGET=$TARGET

cd /sys/class/gpio/gpio110
config-pin P9_31 gpio
echo out > direction
