/**
 * @file   gpio_test.c
 * @author Derek Molloy
 * @date   19 April 2015
 * @brief  A kernel module for controlling a GPIO LED/button pair. The device mounts devices via
 * sysfs /sys/class/gpio/gpio115 and gpio49. Therefore, this test LKM circuit assumes that an LED
 * is attached to GPIO 49 which is on P9_23 and the button is attached to GPIO 115 on P9_27. There
 * is no requirement for a custom overlay, as the pins are in their default mux mode states.
 * @see http://www.derekmolloy.ie/
*/

// Edited by James Werne on 10/11/2020
// P8_15 (button) gets mapped to P9_12 (LED), and P8_18 (button) gets mapped to P9_14 (LED).

#include <linux/init.h>
#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/gpio.h>                 // Required for the GPIO functions
#include <linux/interrupt.h>            // Required for the IRQ code

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Derek Molloy");
MODULE_DESCRIPTION("A Button/LED test driver for the BBB");
MODULE_VERSION("0.1");

static unsigned int gpioLED1 = 60;       ///< hard coding the LED gpio for this example to P9_12 (GPIO60)
static unsigned int gpioLED2 = 50; 	 ///< hard coding the LED gpio to P9_14 (GPIO50)
static unsigned int gpioButton1 = 47;   ///< hard coding the button gpio for this example to P8_15 (GPIO47)
static unsigned int gpioButton2 = 65;	///< hard coding the button gpio to P8_18 (GPIO65)
static unsigned int irqNumber1;          ///< Used to share the IRQ number for button 1 within this file
static unsigned int irqNumber2;
static unsigned int numberPresses = 0;  ///< For information, store the number of button presses
static bool	    ledOn1 = 0;          ///< Is the LED on or off? Used to invert its state (off by default)
static bool 	    ledOn2 = 0;

/// Function prototype for the custom IRQ handler function -- see below for the implementation
static irq_handler_t  ebbgpio_irq_handler(unsigned int irq, void *dev_id, struct pt_regs *regs);


/** @brief The LKM initialization function
 *  The static keyword restricts the visibility of the function to within this C file. The __init
 *  macro means that for a built-in driver (not a LKM) the function is only used at initialization
 *  time and that it can be discarded and its memory freed up after that point. In this example this
 *  function sets up the GPIOs and the IRQ
 *  @return returns 0 if successful
 */
static int __init ebbgpio_init(void){
   int result = 0;
   printk(KERN_INFO "GPIO_TEST: Initializing the GPIO_TEST LKM\n");
   // Is the GPIO a valid GPIO number (e.g., the BBB has 4x32 but not all available)
   if (!gpio_is_valid(gpioLED1)){
      printk(KERN_INFO "GPIO_TEST: invalid LED GPIO\n");
      return -ENODEV;
   }
   if (!gpio_is_valid(gpioLED2)){
      printk(KERN_INFO "GPIO_TEST: invalid LED GPIO\n");
      return -ENODEV;
   }

   // Going to set up the LED. It is a GPIO in output mode and will be on by default
   // 		LED1 & BUTTON1 SETUP
   ledOn1 = true;
   gpio_request(gpioLED1, "sysfs");          // gpioLED is hardcoded to 60, request it
   gpio_direction_output(gpioLED1, ledOn1);   // Set the gpio to be in output mode and on
// gpio_set_value(gpioLED1, ledOn1);          // Not required as set by line above (here for reference)
   gpio_export(gpioLED1, false);             // Causes gpio60 to appear in /sys/class/gpio
			                    // the bool argument prevents the direction from being changed
   gpio_request(gpioButton1, "sysfs");       // Set up the gpioButton
   gpio_direction_input(gpioButton1);        // Set the button GPIO to be an input
   gpio_set_debounce(gpioButton1, 200);      // Debounce the button with a delay of 200ms
   gpio_export(gpioButton1, false);          // Causes gpio115 to appear in /sys/class/gpio
			                    // the bool argument prevents the direction from being changed
   
   // 		LED2 & BUTTON2 SETUP
   ledOn2 = true;
   gpio_request(gpioLED2, "sysfs");          // gpioLED is hardcoded to 50, request it
   gpio_direction_output(gpioLED2, ledOn2);   // Set the gpio to be in output mode and on
// gpio_set_value(gpioLED2, ledOn2);          // Not required as set by line above (here for reference)
   gpio_export(gpioLED2, false);             // Causes gpio50 to appear in /sys/class/gpio
			                    // the bool argument prevents the direction from being changed
   gpio_request(gpioButton2, "sysfs");       // Set up the gpioButton
   gpio_direction_input(gpioButton2);        // Set the button GPIO to be an input
   gpio_set_debounce(gpioButton2, 200);      // Debounce the button with a delay of 200ms
   gpio_export(gpioButton2, false);          // Causes gpio115 to appear in /sys/class/gpio
			                    // the bool argument prevents the direction from being changed

					    
   // Perform a quick test to see that the button is working as expected on LKM load
   printk(KERN_INFO "GPIO_TEST: The button1 state is currently: %d\n", gpio_get_value(gpioButton1));
   printk(KERN_INFO "GPIO_TEST: The button2 state is currently: %d\n", gpio_get_value(gpioButton2));


   // GPIO numbers and IRQ numbers are not the same! This function performs the mapping for us
   irqNumber1 = gpio_to_irq(gpioButton1);
   irqNumber2 = gpio_to_irq(gpioButton2);
   printk(KERN_INFO "GPIO_TEST: Button1 is mapped to IRQ: %d\n", irqNumber1);
   printk(KERN_INFO "GPIO_TEST: Button2 is mapped to IRQ: %d\n", irqNumber2);


   // This next call requests an interrupt line if button2 is pressed
   result = request_irq(irqNumber2,             // The interrupt number requested
                        (irq_handler_t) ebbgpio_irq_handler, // The pointer to the handler function below
                        IRQF_TRIGGER_RISING + IRQF_TRIGGER_FALLING,   // Interrupt on both rising and falling edges (button press & release)
                        "ebb_gpio_handler",    // Used in /proc/interrupts to identify the owner
                        NULL);                 // The *dev_id for shared interrupt lines, NULL is okay

   // This next call requests an interrupt line if button1 is pressed
   result = request_irq(irqNumber1,             // The interrupt number requested
                        (irq_handler_t) ebbgpio_irq_handler, // The pointer to the handler function below
                        IRQF_TRIGGER_RISING + IRQF_TRIGGER_FALLING,   // Interrupt on both rising and falling edges (button press & release)
                        "ebb_gpio_handler",    // Used in /proc/interrupts to identify the owner
                        NULL);                 // The *dev_id for shared interrupt lines, NULL is okay

   printk(KERN_INFO "GPIO_TEST: The interrupt request result is: %d\n", result);
   return result;



}

/** @brief The LKM cleanup function
 *  Similar to the initialization function, it is static. The __exit macro notifies that if this
 *  code is used for a built-in driver (not a LKM) that this function is not required. Used to release the
 *  GPIOs and display cleanup messages.
 */
static void __exit ebbgpio_exit(void){
   printk(KERN_INFO "GPIO_TEST: Button1 state is currently: %d\n", gpio_get_value(gpioButton1));
   gpio_set_value(gpioLED1, 0);              // Turn LED1 off, makes it clear the device was unloaded
   gpio_unexport(gpioLED1);                  // Unexport the LED1 GPIO
   free_irq(irqNumber1, NULL);               // Free the IRQ1 number, no *dev_id required in this case
   gpio_unexport(gpioButton1);               // Unexport the Button1 GPIO
   gpio_free(gpioLED1);                      // Free the LED1 GPIO
   gpio_free(gpioButton1);                   // Free the Button1 GPIO
   printk(KERN_INFO "GPIO_TEST: Goodbye from the LKM!\n");

   printk(KERN_INFO "GPIO_TEST: Button2 state is currently: %d\n", gpio_get_value(gpioButton2));
   gpio_set_value(gpioLED2, 0);              // Turn LED2 off, makes it clear the device was unloaded
   gpio_unexport(gpioLED2);                  // Unexport the LED2 GPIO
   free_irq(irqNumber2, NULL);               // Free the IRQ2 number, no *dev_id required in this case
   gpio_unexport(gpioButton2);               // Unexport the Button2 GPIO
   gpio_free(gpioLED2);                      // Free the LED2 GPIO
   gpio_free(gpioButton2);                   // Free the Button2 GPIO
   printk(KERN_INFO "GPIO_TEST: Goodbye from the LKM!\n");
}

/** @brief The GPIO IRQ Handler function
 *  This function is a custom interrupt handler that is attached to the GPIO above. The same interrupt
 *  handler cannot be invoked concurrently as the interrupt line is masked out until the function is complete.
 *  This function is static as it should not be invoked directly from outside of this file.
 *  @param irq    the IRQ number that is associated with the GPIO -- useful for logging.
 *  @param dev_id the *dev_id that is provided -- can be used to identify which device caused the interrupt
 *  Not used in this example as NULL is passed.
 *  @param regs   h/w specific register values -- only really ever used for debugging.
 *  return returns IRQ_HANDLED if successful -- should return IRQ_NONE otherwise.
 */
static irq_handler_t  ebbgpio_irq_handler(unsigned int irq, void *dev_id, struct pt_regs *regs){
   
   if (irq == irqNumber1) {
	ledOn1 = !ledOn1;                          // Invert the LED1 state on each button press
   	gpio_set_value(gpioLED1, ledOn1);          // Set the physical LED accordingly
   	printk(KERN_INFO "GPIO_TEST: Interrupt! (button1 state is %d)\n", gpio_get_value(gpioButton1));
   	numberPresses++;                         // Global counter, will be outputted when the module is unloaded
   	return (irq_handler_t) IRQ_HANDLED;}      // Announce that the IRQ has been handled correctly
   if (irq == irqNumber2) {
	ledOn2 = !ledOn2;                          // Invert the LED2 state on each button press
   	gpio_set_value(gpioLED2, ledOn2);          // Set the physical LED accordingly
   	printk(KERN_INFO "GPIO_TEST: Interrupt! (button2 state is %d)\n", gpio_get_value(gpioButton2));
   	numberPresses++;                         // Global counter, will be outputted when the module is unloaded
   	return (irq_handler_t) IRQ_HANDLED;}      // Announce that the IRQ has been handled correctly
}


/// This next calls are  mandatory -- they identify the initialization function
/// and the cleanup function (as above).
module_init(ebbgpio_init);
module_exit(ebbgpio_exit);
