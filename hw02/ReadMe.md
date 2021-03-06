# hw02 grading

| Points      | Description |
| ----------- | ----------- |
|  2 | Buttons and LEDs 
|  7 | Etch-a-Sketch works
|    | Measuring a gpio pin on an Oscilloscope 
|  4 | Questions answered
|  2 | Table complete
|  2 | gpiod
|    | Security
|  1 | ssh port
|  1 | iptables
|  1 | fail2ban
| 20 | **Total**

*Well done*

James Werne 
hw02 ReadMe

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

After adding lseek, I noticed considerable improvement in toggling speeds, particularly when reaching the microsecond range. At this point, the shortest periods I could get were at about 300 us; however, with the modified C code, I was able to get as small as 170 us periods. Below the ms range I noticed vast speed improvements, but above the ms range the speed improvements were negligible. The most impressive improvement offered by this C code, however, lies in the decreased processor usage. Even at its fastest, the C script used 60-70% of the CPU; this modified script uses 30-40%.


gpiod: 

Measured the toggle frequency/period of the provided toggle1.c, toggle1.py, toggle2.c, and toggle2.py programs. Recorded all measurements in the "Oscilloscope_Measurements.txt" document provided in this repository.



security:

I set it so that I now ssh into the bone using port 1022 (had to change setDNS.sh, firstssh.sh, and the sshd config file given in the instructions).
I added a command to my iptables to allow ssh into port 3000 on the Bone from the ip of the computer, then I appended a rule to drop all other ssh requests.
Downloaded fail2ban and edited the jail.local file to reject ssh connections for 15 seconds after 2 failed attempts.



Etch-a-sketch: 

I made it so that the dimensions and the game are now both controlled using the pushbuttons. 
To enter the dimensions, use the leftmost pushbutton to decrease dimension and the middle left pushbutton to increase dimension. Use rightmost pushbutton to confirm dimension. To control the game, use the leftmost pushbutton to move left, left middle pushbutton to move up, right middle pushbutton to move down, and rightmost pushbutton to move right. 
Note that for the time being, I've decided to not include diagonal movement (for simplicity's sake). To exit the game, press Ctrl+C on the keyboard.



Modifications:

togglegpio.c: 

Modified the file. It's included as togglegpio_modified.c. If you want to run 10000 us on and 50000 us off on pin line 60, run ./togglegpio_modified 60 10000 50000.

3) The highest frequency on the scope is 3.320 kHz.

gpio-int-test.c 

Modified the file. It's included as gpio-int-test_modified.c. If you want to run the code on gpio 60, run ./gpio-int-test_modified 60. Next, I created gpioThru.c and made it so that the user can enter an input signal pin and an output signal pin. If you want to copy the value of port 7 to port 60, run ./gpioThru 7 60.

3) The output does track the input.
4) The highest frequency the output will consistently track is about 200 Hz, otherwise the pulse widths start to vary wildly. However, the frequency has gone as high as 600 Hz, but it's incredibly inconsistent. At 200 Hz, the processor is at 78% usage; any higher, the processor quickly hits 100% usage.
5) The delays are somewhat inconsistent, for me. I found the delay for a rising edge hovers right around 900 us, whereas the falling edge delay is closer to 1.5 ms. I measured several different edges at 100 Hz, and that was the trend I saw in the scope readings.


--------------------------------------------------------------------
James Werne
Oscilloscope Measurements

| Oscilloscope Measurements | Period1    | CPU1 Usage | Period2    | CPU2 Usage | Period3    | CPU3 Usage | Period4    | CPU4 Usage |
| :---                      | ---        | ---        | ---        | ---        | ---        | ---        | ---        | ---        |
| Type:                     | Shell      | Shell      | Python     | Python     | C          | C          | CModified  | CModified  |
| 100 ms                    | 244.4 ms   | 19.60%     | 200.6 ms   | 3.30%      | 200.4 ms   | 3.30%      | 200.2 ms   | 2.60%      |
| 50 ms                     | 143.4 ms   | 32.50%     | 100.5 ms   | 3.30%      | 100.4 ms   | 3.30%      | 100.2 ms   | 2.60%      |
| 25 ms                     | 92.12 ms   | 48.70%     | 50.48 ms   | 3.30%      | 50.4 ms    | 3.90%      | 50.24 ms   | 2.60%      |
| 10 ms                     | 63.00 ms   | 70.50%     | 20.48 ms   | 4.00%      | 20.34 ms   | 4.60%      | 20.18 ms   | 3.30%      |
| 1 ms                      | 45.48 ms   | 96.10%     | 2.402 ms   | 12.90%     | 2.318 ms   | 13.50%     | 2.182 ms   | 3.40%      |
| 100 us                    | 43.2 ms    | 99.40%     | 568.4 us   | 41.20%     | 500.8 us   | 40.70%     | 375.8 us   | 16.30%     |
| 1 us                      | NA         | NA         | 370.0 us   | 77.00%     | 300.1 us   | 61.90%     | 178.5 us   | 33.90%     |


| Osciloscope Measurements | Toggle1.c        | Toggle1.py        | Toggle2.c pin 14 | Toggle2.c pin 16 | Toggle2.py pin 14 | Toggle2.py pin 16 |
| :---                     | ---              | ---               | ---              | ---              | ---               | ---               |
| Period:                  | 3.350 us         | 17.37 us          | 3.580 us         | 3.580 us         | 17.90 us          | 17.90 us          |
| Frequency:               | 298.5 kHz        | 57.57 kHz         | 279.3 kHz        | 279.3 kHz        | 55.87 kHz         | 55.87 kHz         |
