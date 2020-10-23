# hw05 grading

| Points      | Description |
| ----------- | ----------- |
|  2 | Project - *Sudoku looks like a hard one, unless you already have the solver.*
|  2 | Makefile
|  4 | Kernel Source
|  2 | Cross-Compiling
|  8 | Kernel Modules: hello, ebbchar, gpio_test, led
|  1 | Extras
| 19 | **Total**

*My comments are in italics. --may*

James Werne
ECE434 HW05
ReadMe


Project:

I've attached the word document 'Projects 2020 (HW5).docx' in my repo. I've placed my name next to the projects I'm interested in working on, and I added a project idea involving Bluetooth footage transfer from a camera to a smartphone. Note that Neil Roy is my project partner, so we will work together.

*No need to attach.  I see you've added your ideas to the original.*

Make:

I copied the "make" directory from the provided "exercises" repo and modified the script to generate .o files from .c files, then compiled those .o files into .arm files (using user-defined and built-in variables).
To compile, simply type "make" or "make all" in the command line. To remove the compiled files, run "make clean". To get more information about the variables used, type "make test". Once the files are compiled, run "app.arm" to print "Hello World" into the command line.



Installing the Kernel Source:

The kernel I installed is version 5.8.10-bone16.



Cross-Compiling:

I installed v5.8 of the Linux Kernel, then compiled helloWorld.c on the host computer and sent the compiled file to the Bone. The compiled file is in this repo and is named "a.out"

Output on Bone:
```
Hello, World! Main is executing at 0x10495
This address (0xbef1e538) is in our stack frame
This address (0x21038) is in our bss section
This address (0x2102c) is inour data section
```

Output on Host:
```Hello, World! Main is executing at 0x400596
This address (0x7fffee0c88c0) is in our stack frame
This address (0x601048) is in our bss section
This address (0x601040) is in our data section
```


Kernel Modules: 

Basic info: The necessary modules for hello, ebbchar, and gpio_test are given in folders of the same name in this repo. Each respective module has a .ko extension and can be inserted by running "sudo insmod <file>.ko". If necessary, run "make" in the command line before inserting the module.

Running "sudo insmod hello.ko" will print "Hello World" to the kernel log file. To view this, run "dmesg -H | tail -1". If you want to have the script address you by name, run "sudo insmod hello.ko name="Your Name"".

Running "sudo insmod ebbchar.ko", then "sudo ./test"  will prompt you to type a string into the command line, which is then sent and returned from the kernel.

If in the "gpio_test_valuecopy" folder, running "sudo insmod gpio_test.ko" will guarantee that when you press the pushbutton attached to "P9_15", the LED attached to "P9_16" will immediately turn off in response. Releasing the pushbutton turns on the LED.

If in the "gpio_test_twoinputs" folder, running "sudo insmod gpio_test.ko" will guarantee that when you press the pushbutton attached to "P8_15", the LED attached to "P9_12" will turn off. Similarly, pressing the pushbutton attached to "P8_18" will turn on the LED at "P9_14" off.

Note that gpio_test_valuecopy is the module that copies the value of P9_15 (a pushbutton) to P9_16 (an LED). Additionally, gpio_test_twoinputs maps a pushbutton at P8_15 to an LED at P9_12; similarly, P8_18 is mapped to P9_14.


A-level info: I modified the led.c file to have two LEDs (P9_12 and P9_14) blink at different rates. I did this by creating two separate kthreads and setting them to run in parallel. This module is located in the folder "led_differentrates". Just as with the above modules, this led module can be inserted by running "sudo insmod led.ko".

To dismount a module, run "sudo rmmod <filename>".
