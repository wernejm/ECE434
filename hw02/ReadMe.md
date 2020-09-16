James Werne hw02 ReadMe


This is a ReadMe outlining the contents of the hw02 repository. 

Buttons and LEDs:
I've written a program called "buttons_leds.py" that uses events/callbacks to detect when a pushbutton is pressed. When one of four pushbuttons is pressed, it lights up a corresponding LED. To test this, run ./buttons_leds.py in the terminal; to kill the program, press Ctrl+C.



Measuring a gpio pin on an Oscilloscope:
All of the table results are included in "Oscilloscope_Measurements.txt". View using any preferred text editor. All of the following programs apply to gpio60.

Shell:
The answers to the shell script questions are included in "hw02_Questions_shell.txt". All of these measurements were made by using the provided togglegpio.sh file in the exercises/gpio directory.

Python:
The answers to the python questions are included in "hw02_Questions_python.txt". All of these measurements were made using a program a I wrote: "togglegpio.py". To execute, run ./togglegpio.py in the terminal and follow the instructions: to kill, press Ctrl+C.

C:
The answers to the C questions are included in "hw02_Questions_c.txt". The first set of measurements was made using the provided togglegpio.c file in the exercises/gpio directory, while the second set of measurements was made by removing the fd_open and fd_close statements and replacing them with an lseek() command. This program is included in this repository as "togglegpio_lseek". To execute, run ./togglegpio_lseek 100, where 100 is the sleep time in microseconds.

After adding lseek, I found that there wasn't any improvement in toggling speed, and it actually increased CPU usage. I think it's worth noting that this was the last measurement I made in the session, and my Bone started to run a little slower/more inconsistently, so it might be a hardware/heating issue rather than a software issue.



gpiod:
Measured the toggle frequency/period of the provided toggle1.c, toggle1.py, toggle2.c, and toggle2.py programs. Recorded all measurements in the "Oscilloscope_Measurements.txt" document provided in this repository.



security:
1) I set it so that I now ssh into the bone using port 1022 (had to change setDNS.sh, firstssh.sh, and the sshd config file given in the instructions).
2) I added a command to my iptables to allow ssh into port 3000 on the Bone from the ip of the computer, then I appended a rule to drop all other ssh requests.
3) Downloaded fail2ban and edited the jail.local file to reject ssh connections for 15 seconds after 2 failed attempts. 



Etch-a-sketch:
I made it so that the dimensions and the game are now both controlled using the pushbuttons.
To enter the dimensions, use the leftmost pushbutton to decrease dimension and the middle left pushbutton to increase dimension. Use rightmost pushbutton to confirm dimension.
To control the game, use the leftmost pushbutton to move left, left middle pushbutton to move up, right middle pushbutton to move down, and rightmost pushbutton to move right. Note that for the time being, I've decided to not include diagonal movement (for simplicity's sake). To exit the game, press Ctrl+C on the keyboard.


Modifications:

   togglegpio.c:
Modified the file. It's included as togglegpio_modified.c. If you want to run 10000 us on and 50000 us off on pin line 60, run ./togglegpio_modified 60 10000 50000.

4) The highest frequency on the scope is 3.320 kHz.


   gpio-int-test.c
Modified the file. It's included as gpio-int-test_modified.c. If you want to run the code on gpio 60, run ./gpio-int-test_modified 60.
Next, I created gpioThru.c and made it so that the user can enter an input signal pin and an output signal pin. If you want to copy the value of port 7 to port 60, run ./gpioThru 7 60.

3) The output does track the input.
4) The highest frequency the output will consistently track is about 200 Hz, otherwise the pulse widths start to vary wildly. However, the frequency has gone as high as 600 Hz, but it's incredibly inconsistent. At 200 Hz, the processor is at 78% usage; any higher, the processor quickly hits 100% usage.
5) The delays are somewhat inconsistent, for me. I found the delay for a rising edge hovers right around 900 us, whereas the falling edge delay is closer to 1.5 ms. I measured several different edges at 100 Hz, and that was the trend I saw in the scope readings.
