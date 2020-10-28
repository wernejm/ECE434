#include <stdint.h>
#include <pru_cfg.h>
#include "resource_table_empty.h"
#include "prugpio.h"

volatile register unsigned int __R30;
volatile register unsigned int __R31;

// Modified by James Werne, 10/28/2020
// Changed it to toggle P9_31 as fast as possible

void main(void) {
	int i;

	uint32_t *gpio3 = (uint32_t *)GPIO3;
	
	/* Clear SYSCFG[STANDBY_INIT] to enable OCP master port */
	CT_CFG.SYSCFG_bit.STANDBY_INIT = 0;
	
	int pin31 = 1<<14;	// P9_31 is given by gpio3[14]
	
	while(1) {
	//for(i=0; i<10; i++) {
		gpio3[GPIO_SETDATAOUT]   = pin31;	// The the USR3 LED on

	//	__delay_cycles(500000000/5);    	
		__delay_cycles(0);					// wait 0 seconds
		gpio3[GPIO_CLEARDATAOUT] = pin31;
		__delay_cycles(0);
	//	__delay_cycles(500000000/5); 

	}
	__halt();
}

// Turns off triggers
#pragma DATA_SECTION(init_pins, ".init_pins")
#pragma RETAIN(init_pins)
const char init_pins[] =  
	"/sys/class/leds/beaglebone:green:usr3/trigger\0none\0" \
	"\0\0";
