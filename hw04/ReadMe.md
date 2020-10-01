James Werne
ECE434 Embedded Linux
hw04 ReadMe

The following outlines the files contained in the hw04 directory:


Memory Map:

The file containing the drawing is named ECE434_Memory_Map.jpg. Open this to view the mapping I drew for the Bone.


GPIO via mmap

Press one of two pushbuttons to turn on a corresponding LED ("P9_30" maps to USR1 LED, and "P9_41" maps to USR3 LED). To run this program, execute "mmap_leds_switches.py" (note: this must be run as sudo).

This folder also includes a script that toggles a GPIO pin (P9_30, in this case) as fast as possible using mmap. To run this program, execute "mmap_gpio_toggle.py".
When I enter a sleep time of 1 ns between toggles, I measured that the period of the output is 200.5 us, which is considerably faster than the 370us speed we measured from hw02 for the python toggling script. Using htop, it appears this scipt
is at 53.4% CPU usage when using the above sleep time (note that making the sleep time even smaller does not increase CPU usage, nor does it improve the toggling period).
Without a sleep time, I measured the period to be 10.97 us. This is much faster than the above script with the time.sleep included. This is also considerably faster than even the gpiod python script from hw02, which peaked at 17.37us. Additionally, 
using htop, this gives a CPU usage of 100%.



i2c via the Kernel Driver

If you've just connected to the bone, you must first run "i2c_kernel_tmpsetup.sh" to add the tmp101 device's address to the kernel. To read the temperatures for the left and right sensor, run "i2c_kernel_read.sh", and the values will be printed to the terminal.



Control the LED matrix from a browser

I used Flask to interface a web browser with the LED matrix etch-a-sketch game implemented last week. To play this game, run "etchasketch_hw4_flask.py", then open a web browser and navigate to "192.168.7.2:8081". Press the buttons shown on the screen to move the etch-a-sketch dot in the corresponding direction.



2.4" TFTLCD Display

I installed several programs to view images, display text, and play videos.
In order to rotate the screen, run the "on_rotated.sh" script contained in this repo. I've attached an example film, image, and text script to display this feature.
To display an image of Boris, run the following command: "sudo fbi -noverbose -T 1 -a boris.png"
To display the movie "hst_1.mpg", run the following command: "mplayer -vf-add rotate=4 -framedrop hst_1.mpg"
To display the my signature, run "text.sh" in the command window.

I took pictures of the rotated Boris image, the rotated movie, and the rotated text. These piectures have been included as "Boris_Rotated.jpg", "Movie_Rotated.jpg", and "Text_Rotated.jpg", respectively.
