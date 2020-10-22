James Werne
ECE434 hw07 readme


Note: Neil Roy and I created an eLinux page dedicated to our final project. We're planning to interface a phone to a bluetooth speaker using the beaglebone's wireless capabilities as an interface. We're also planning on having LEDs that respond to the lights, as well as a blynk interface that allows for additional eq/mixing options.


Blynk:

I downloaded blynk & set up the authorization code in setup.sh to connect to my phone. If I run the project on my phone and execute leds.py (or leds2.py) on the Bone, I'm able to use the virtual button to blink the USR3 LED, and I'm able to press the physical pushbutton attached to "P9_11" to blink a virtual LED.


A Temperature Display:

I added a "Value Display" widget, attached it to a virtual pin, then modified my code from hw03 to write the TMP101 temperature to that virtual pin. To execute this code, run "Temp_Blynk_Read".


Etch-a-sketch

I used blynk to control my LED matrix etch-a-sketch game. To run this, execute "etchasketch_hw7_blynk.py" in the command line and play away!
