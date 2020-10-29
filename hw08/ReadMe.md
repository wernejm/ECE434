James Werne
ECE434
hw08 ReadMe

PRU:

I cloned the repository, as instructed by the Getting Example Code page. I then did each of the examples (Blinking an LED, PWM Generator, Controlling the PWM frequency, Reading an Input at Regular Intervals, and Analog Wave Generator). I've reported my results below.


2.6 Blinking an LED:

To get the pru code running in the example, I had to run make TARGET=hello.pru0 which executed the code and blinked the USR3 LED ten times. In order to stop PRU code from running, the example suggests that "halt()" is the command that stops it.
I edited the hello.pru0 code to toggle P9_31 using the same method as the example code. I also set delay cycles to 0 and measured how fast I could toggle the pin (using an oscillocope). To run this code, navigate to the "Blinking_LED" subdirectory, then run ./setup.sh and run "make TARGET=hello.pru0".


Questions: How fast can you toggle the pin? Is there jitter? Is it stable?

I measured the max frequency of the toggle to be 12.5 Mhz. There doesn't appear to be any significant jitter, as each wave has a pretty uniform 50% duty cycle; however, the wave has a decent bit of ripple/overshoot, so it's not a perfect square wave. It does appear to be stable, as the waveform doesn't appear to be shifting or jumping around at all.
![Alt text](/hw08_Blinking_LED.jpg?raw=true "Title")


5.3 PWM Generator:

I ran the pwm1.pru0.c code (note that the output was already set to P9_31). I changed the frequency of the pulse to 50MHz as specified. To run this code, navigate to the "PWM Generator" subdirectory, then run ./shared_setup.sh and run "make TARGET=pwm1.pru0".

Questions: How stable is the waveform. What's the standard deviation? Is there jitter?

I took a picture of the oscilloscope reading on my phone -- the waveform itself doesn't resemble a square wave at all (looks more like a sinusoid). It's a fairly steady waveform, though, so it appears to be stable (not jumping around). Aside from the fact that the waveform doesn't look like a square wave, there doesn't appear to be any jitter; the signal is periodic at about 50 MHz, and it holds its periodicity well.
From my scope capture, I measured the Std. Dev to be about 110.8 kHz.



5.4 Controlling the PWM Frequency

I went through the example & reported my results below. To run this code, navigate to the "PWM_Frequency" subdirectory, then run ./pwm_setup.sh and run "make TARGET=pwm4.pru0.c"

Questions: What output pins are being driven? What's the highest frequency you can get with four channels? Is there jitter? Run the pwm-test.c program to change the on and off times. Does it work?

In the code provided for pwm4.pru0.c, MAXCH is set to 4, which means channels 0, 1, 2, and 3 are being used as outputs (these correspond to P9_31, P9_30, P9_29, and P9_28 respectively). I set the delays to 1 on and 1 off, and I was able to get a maximum frequency of about 735 kHz. However, the distances between each pulse are not equal, so the waveform isn't exactly periodic, so there is some jitter with this signal (I have a picture of the oscilloscope on my phone).

I then modified the pwm-test.c code to have the countOn be equal to 2 and countOff equal to 5 for each channel. After saving, making the file, and running pwm-test.out, the oscilloscope shows that the output signal's on/off times did indeed change as a result of the code. To see this, run "make TARGET=pwm-test" and then "sudo ./pwm-test.out".



5.9 Reading an Input at Regular Intervals

I went through the example & reported how fast the code could transfer the info from input to output (P9_31). To run the code, navigate to the "Input_Regular_Intervals" subdirectory, then run ./input_setup.sh, then run "make TARGET=input.pru0" to actually write values from input to the output.

Questions: Use a function generator and an oscilloscope to see how fast the code can transfer the input to the output. 

The function generator only goes up to 12.5 MHz, and the oscilloscope reading at the output accurately reads 12.5 MHz. As a result, the input.pru0.c code toggles at a minimum speed of 12.5 MHz.



5.10 Analog Wave Generator

I went through the example & reported my results. To run the code, navigate to teh "Analog_Wave_Generator" subdirectory, then run ./shared_setup.sh, then run "make TARGET=sine.pru0" to generate the waveform. 


The unfiltered sawtooth wave produced an odd result; during the high duty cycle, the scope shows what looks like a bunch of sine waves superimposed over each other; there are several back-to-back rising edges without any falling edges. This is for the first part of the duty cycle (positive); the other part of the cycle is mostly zero, with a few rising edges popping up occasionally. I have a picture on my phone; this suggests a very unstable waveform.

I implemented a first-order low pass filter using a 22 uF capacitor and a potentiometer. By tweaking the potentiometer, I was able to get a signal that much more closely resembles a sawtooth wave (with a little jitter and some high frequencies creating a fuzzy rising edge, but much better than the signal without the filter). Using the given code, the sawtooth wave has a frequency of about 6.1 kHZ. If I decrease the number of samples to, say, 30, I get a sawtooth with a jagged rising edge (which could certainly be filtered out) that reaches 25.7 kHz. I wouldn't personally go much lower than 30 samples, though.

I tested the triangle and sine waveforms as well. I was able to get a clean triangle signal using 100 samples (and the first order filter from above). One interesting thing I noticed is that if you use an odd/peculiar number of samples (like 105), the signal being generated doesn't play nicely. I noticed there was an odd dip toward the peak of the rising edge whenever I used 105 samples, and I thought it was worth noting.

For the sine waveform, I was able to get a clean sine wave using 100 samples (and the first order filter from above). I have pictures of each of the above oscilloscope waveforms on my phone.

Out of curiosity, I compared the amount of instruction memory being used by each waveform. With 100 samples, the sawtooth uses 0x01bc bytes (444); the triangle uses 0x01cc (460 bytes); the sinusoid uses 0x18c0 bytes (6336), which is a result of the floating point used to store the values needed to generate the waveform.
