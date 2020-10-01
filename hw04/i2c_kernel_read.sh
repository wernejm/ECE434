#!/bin/sh
# i2c_kernel_read
# The following script reads the TMP101 sensors using the kernel driver
# If the tmp sensors haven't been set up yet, run tmp101_kernel_setup.sh before #    running this script

cd /sys/class/i2c-adapter/i2c-2/2-0048/hwmon/hwmon0/
tmpa=$( cat temp1_input )
echo "TMP101 Left: " $tmpa "(milli-degrees Celsius)"
cd /sys/class/i2c-adapter/i2c-2/2-004a/hwmon/hwmon1/
tmpb=$( cat temp1_input )
echo "TMP101 Right: " $tmpb "(milli-degrees Celsius)"
