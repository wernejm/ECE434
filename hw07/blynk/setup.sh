export BLYNK_AUTH='rYgNKhI4DNc0SlWErt4cVjsWCgmwI3nM'

# If useing BMP085 Temp/Pressure sensor

I2C=/sys/class/i2c-adapter/i2c-2
echo bmp085 0x77 > $I2C/new_device
