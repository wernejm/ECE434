#!/bin/sh
# i2c_kernel_tmpsetup
# James Werne
# This script registers the temp101 sensors at addresses 0x48 and 0x4a

cd /sys/class/i2c-adapter/i2c-2
echo tmp101 0x48 > new_device
echo tmp101 0x4a > new_device
