James Werne
ECE434 HW06
ReadMe


Projects:

I added another project to the project document I submitted for hw05. This can be viewed under 'Projects 2020 (HW6).docx' or under Projects.docx.


Watch:

Answers to RTOS questions are given below.
1. Julia Cartwright works at National Instruments.
2. PREEMPT_RT is a patch that converts Linux into a real-time operating system. Linux itself is filled with countless unbounded latencies, and PREEMPT_RT attempts to put bounds on as many of those applications as possible (so that when something needs to get done, it gets done in the time needed).
3. Mixed criticality refers to tasks with differing degrees of time-sensitivity that could run/interact together (i.e. not all tasks are equally important/time-sensitive).
4. The driver stacks are shared between the Linux kernel and the PREEMPT_RT kernel, which can cause several issues if the Linux kernel isn't sufficiently handling RT and non-RT tasks separately. In particular, pay attention to whether the drivers are involved in interrupt dispath or scheduling.
5. The delta is the time it takes from an event ocurring (whether it be sensor input or interrupt firing off) to the system's actual response (the task/application being executed)
6. Cyclictest is a way to accurately and repeatedly measure the delta (see above) of a task. This helps to statistically characterize latencies of an OS.
7. The plot in Figure 2 shows two different cyclictest distributions; the purple shows how long a particular task takes to run on a mainline kernel, where the green is how long it takes to run that same task on the same machine using the PREEMPT_RT patch. As can be seen, the mainline kernel doesn't appear to have much of a bound on the delta, so the distribution is spread out much further. For the RT patch, the distribution of deltas is much tighter and tends toward lower latencies.
8. Dispatch latency: the amount of time between the hardware firing and the relevant thread being "woken up". Scheduling latency: the amount of time between the scheduler recognizing the task/waking up the thread and the CPU actually receiving the task to be executed.
9. Mainline refers to the most up-to-date version of the Linux kernel. This is the one being edited by Linus Torvalds and contains the most recent features/patches. After several months, the mainline kernel is considered to be "stable" as kernel maintainers fix bugs and other issues.
10. The low-priority interrupt (non critical IRQ) has to finish executing in a mainline kernel before anything else can be accomplished by the CPU. In this case, the external event cannot start until the low-priority intterupt has been handled.
11. With the RT patch, IRQ threads are forced; these effectively wake up the interrupt handlers, which by nature are more efficient and more timely than the non critical interrupts from the mainline kernel. As a result, this means that less time is spent handling interrupts, which means that if a high priority interrupt is fired (in this case, an external event), it can be scheduled much more quickly and threaded.



PREEMPT_RT: 

I installed the PREEMPT_RT real-time kernel and ran several cyclictests to compare the deltas of the mainline/stable kernel and the RT patch. 

I used two cases; one involved running the cyclictest with a load, while the other involved running the cyclictest without a load. My "load" was running make/make clean commands back-to-back during the test (specifically in the directory ~/exercises/linux/modules). I've included three PNG plots for each case; one displaying the no RT results (cyclictest_<loadtype>_nort.png), one displaying the RT results (cyclictest_<loadtype>_rt.png), and one that overlaps the two results for comparison.

As can be seen from the plots, the delta for the RT kernel is typically smaller and has a tighter distribution than the delta for the noRT kernel. This is much more apparent with the load; the RT kernel appears to have a bounded latency of about 100-120 us with a load, whereas the noRT kernel does not have a clear bounded latency. In the unloaded case, the RT kernel has a bounded latency of about 80 us, whereas the noRT kernel's bounded *appears* to be 90 us (but could very well be unbounded).
