// Blink pin specified by user at on/off time specified by user
//
// Created by Dingo_aus, 7 January 2009
// email: dingo_aus [at] internode <dot> on /dot/ net
// From http://www.avrfreaks.net/wiki/index.php/Documentation:Linux/GPIO#gpio_framework
//
// Created in AVR32 Studio (version 2.0.2) running on Ubuntu 8.04
// Modified by Mark A. Yoder, 21-July-2011
// Modified by Mark A. Yoder 30-May-2013
// Modified by James Werne, 15-Sept-2020

#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <fcntl.h>
#include "gpio-utils.h"


int keepgoing = 1;	// Set to 0 when ctrl-c is pressed


/**************************************
 * Signal_handler
 * ************************************/
void signal_handler(int sig);
// Callback called when SIGINT is sent to the process (Ctrl-C)
void signal_handler(int sig)
{
	printf( "Ctrl-c pressed, cleaning up and exiting..\n" );
	keepgoing = 0;
}




// three arguments: first is the pin line, second is the time on,
// 	third is the time off.
// e.g. bone$ ./togglegpio_modified 60 1000 1000
int main(int argc, char** argv)
{
	//create a variable to store whether we are sending a '1' or a '0'
	char set_value[5]; 
	//Integer to keep track of whether we want on or off
	int toggle = 0;
	int onTime;	// Time in micro sec to keep the signal on
	int offTime;	// Time in micro sec to keep the signal off
	int gpio = atoi(argv[1]);
	int gpio_fd;

	if (argc < 4) {
		printf("Usage: %s <on/off time in us>\n\n", argv[0]);
		printf("Toggle gpio 60 at the period given\n");
		exit(-1);
	}
	
	// Set signal callback for Ctrl-C
	signal(SIGINT, signal_handler);

	onTime = atoi(argv[2]);
	offTime = atoi(argv[3]);

	printf("**********************************\n"
		"*  Welcome to PIN Blink program  *\n");
	printf( "*  ....blinking gpio %s          *\n", argv[1]);
	printf(	"*  ....on for %d us..............*\n", onTime);
	printf( "*  ....off for %d us.............*\n"
		"**********************************\n", offTime);

	//Using sysfs we need to write the gpio number to /sys/class/gpio/export
	//This will create the folder /sys/class/gpio/gpio60
	gpio_export(gpio);

	printf("...export file accessed, new pin now accessible\n");
	
	//SET DIRECTION
	gpio_set_dir(gpio, "out");
	printf("...direction set to output\n");
			
	gpio_fd = gpio_fd_open(gpio, O_RDONLY);

	//Run an infinite loop - will require Ctrl-C to exit this program
	while(keepgoing)
	{
		toggle = !toggle;
		gpio_set_value(gpio, toggle);
//		printf("...value set to %d...\n", toggle);

		//Pause for a while
		usleep(onTime);

		toggle = !toggle;
		gpio_set_value(gpio, toggle);

		usleep(offTime);
	}
	gpio_fd_close(gpio_fd);
	return 0;
}
