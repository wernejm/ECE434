James Werne hw02 ReadMe


This is a ReadMe outlining the contents of the hw02 repository. 

Section 1: Buttons and LEDs:
I've written a program called "buttons_leds.py" that uses events/callbacks to detect when a pushbutton is pressed. When one of four pushbuttons is pressed, it lights up a corresponding LED. To test this, run ./buttons_leds.py in the terminal; to kill the program, press Ctrl+C.


Section 2: Measuring a gpio pin on an Oscilloscope:
All of the table results are included in "Oscilloscope_Measurements.txt". View using any preferred text editor. All of the following programs apply to gpio60.

Shell:
The answers to the shell script questions are included in "hw02_Questions_shell.txt". All of these measurements were made by using the provided togglegpio.sh file in the exercises/gpio directory.

Python:
The answers to the python questions are included in "hw02_Questions_python.txt". All of these measurements were made using a program a I wrote: "togglegpio.py". To execute, run ./togglegpio.py in the terminal and follow the instructions: to kill, press Ctrl+C.

C:
The answers to the C questions are included in "hw02_Questions_c.txt". The first set of measurements was made using the provided togglegpio.c file in the exercises/gpio directory, while the second set of measurements was made by removing the fd_open and fd_close statements and replacing them with an lseek() command. This program is included in this repository as "togglegpio_lseek". To execute, run ./togglegpio_lseek 100, where 100 is the sleep time in microseconds.


gpiod:


security:
1) I set it so that I now ssh into the bone using port 1022 (had to change setDNS.sh, firstssh.sh, and the sshd config file given in the instructions).
2) 




Etch-a-sketch:
I made it so that the dimensions and the game are now both controlled using the pushbuttons.
To enter the dimensions, use the leftmost pushbutton to decrease dimension and the middle left pushbutton to increase dimension. Use rightmost pushbutton to confirm dimension.
To control the game, use the leftmost pushbutton to move left, left middle pushbutton to move up, right middle pushbutton to move down, and rightmost pushbutton to move right. Note that for the time being, I've decided to not include diagonal movement (for simplicity's sake).


Modifications:
togglegpio.c

gpio-int-test.c
