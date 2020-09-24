James Werne
ECE434 hw03 ReadMe

TMP101:
"What are the addresses the TMP101 uses on the i2c bus?"
- 0x48 and 0x4a (since ADD0 sets the 2nd bit spot, so we have 1001 010 and 1001 000 as the addresses)

There are three temperature-based scripts contained in this directory: TempRead.sh, TempRead.py, and TempAlert.py.

TempRead.sh reads the temperature from the sensor and converts it to Fahrenheit. The script also sets the clock and data pins to i2c pin-muxed mode, so this script should be run before the other scripts.

TempRead.py reads the temperature, converts it to Fahrenheit, and continually updates the value.

TempAlert.py sets temperature limits, sets the sensor to "Alert" mode, then prints the temperature when the temperature exceeds either limit.


Etch-a-sketch:
There are two etch-a-sketch programs in this section:
etchasketch_hw3_ledmatrix.py, which uses pushbuttons to control the game & displays it on the LED matrix, and
etchasketch_hw3_encoder.py, which uses the rotary encoders to control the game.

Before using the rotary encoder, you should first run rotarysetup.sh to set the correct pin-muxing.

Directions for controlling each are included in the code's documentation/in the statements printed to the terminal. 
