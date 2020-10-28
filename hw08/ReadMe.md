James Werne
ECE434
hw08 ReadMe

PRU:

I cloned the repository, as instructed by the Getting Example Code page. I then did each of the examples (Blinking an LED, PWM Generator, Controlling the PWM frequency, Reading an Input at Regular Intervals, and Analog Wave Generator). I've reported my results below and included tables as necessary.


2.6 Blinking an LED:

To get the pru code running in the example, I had to run make TARGET=hello.pru0 which executed the code and blinked the USR3 LED ten times. In order to stop PRU code from running, the makefile suggests that "halt()" is the command that stops it.
I edited the hello.pru0 code to toggle P9_31 using the same method as the example code. I also set delay cycles to 0 and measured how fast I could toggle the pin (using an oscillocope). To run this code, navigate to the "Blinking_LED" subdirectory, then run ./setup.sh and run "make TARGET=hello.pru0".


Questions: How fast can you toggle the pin? Is there jitter? Is it stable?

I measured the max frequency of the toggle to be 12.5 Mhz. There doesn't appear to be any significant jitter, as each wave has a pretty uniform 50% duty cycle; however, the wave has a decent bit of ripple/overshoot, so it's not a perfect square wave. It does appear to be stable, as the waveform doesn't appear to be shifting or jumping around at all.



5.3 PWM Generator:

I ran the pwm1.pru0.c code (note that the output was already set to P9_31). I changed the frequency of the pulse to 50MHz as specified. To run this code, navigate to the "PWM Generator" subdirectory, then run ./shared_setup.sh and run "make TARGET=pwm1.pru0".

Questions: How stable is the waveform. What's the standard deviation? Is there jitter?

I took a picture of the oscilloscope reading on my phone -- the waveform itself doesn't resemble a square wave at all (looks more like a sinusoid). It's a fairly steady waveform, though, so it appears to be stable (not jumping around). Aside from the fact that the waveform doesn't look like a square wave, there doesn't appear to be any jitter; the signal is periodic at about 50 MHz, and it holds its periodicity well.
From my scope capture, I measured the Std. Dev to be about 110.8 kHz.



5.4 Controlling the PWM Frequency

I went through the example & reported my results below. To run this code, navigate to the "PWM_Frequency" subdirectory, then run ./shared_setup.sh and run "make TARGET=pwm4.pru0.c"

Questions: What output pins are being driven? What's the highest frequency you can get with four channels? Is there jitter? Run the pwm-test.c program to change the on and off times. Does it work?





5.9 Reading an Input at Regular Intervals

I went through the example & reported how fast the code could transfer the info from input to output (P9_31). To run the code, navigate to the "Input_Regular_Intervals" subdirectory, then run ./input_setup.sh, then run ./input.c to actually write values from input to the output.

Questions: Use a function generator and an oscilloscope to see how fast the code can transfer the input to the output.



5.10 Analog Wave Generator

I went through the example & reported my results. To run the code, navigate to teh "Analog_Wave_Generator" subdirectory, then run ./shared_setup.sh, then run "make TARGET=sine.pru0" to generate the waveform. 



