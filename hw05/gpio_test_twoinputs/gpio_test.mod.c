#include <linux/module.h>
#define INCLUDE_VERMAGIC
#include <linux/build-salt.h>
#include <linux/vermagic.h>
#include <linux/compiler.h>

BUILD_SALT;

MODULE_INFO(vermagic, VERMAGIC_STRING);
MODULE_INFO(name, KBUILD_MODNAME);

__visible struct module __this_module
__section(.gnu.linkonce.this_module) = {
	.name = KBUILD_MODNAME,
	.init = init_module,
#ifdef CONFIG_MODULE_UNLOAD
	.exit = cleanup_module,
#endif
	.arch = MODULE_ARCH_INIT,
};

#ifdef CONFIG_RETPOLINE
MODULE_INFO(retpoline, "Y");
#endif

static const struct modversion_info ____versions[]
__used __section(__versions) = {
	{ 0x62f7fcee, "module_layout" },
	{ 0xfe990052, "gpio_free" },
	{ 0xc1514a3b, "free_irq" },
	{ 0x58d1f292, "gpiod_unexport" },
	{ 0x92d5838e, "request_threaded_irq" },
	{ 0x6e141adc, "gpiod_to_irq" },
	{ 0x406fe905, "gpiod_set_debounce" },
	{ 0x39bd0e4e, "gpiod_direction_input" },
	{ 0x3349566e, "gpiod_export" },
	{ 0x2308e66c, "gpiod_direction_output_raw" },
	{ 0x47229b5c, "gpio_request" },
	{ 0xefd6cf06, "__aeabi_unwind_cpp_pr0" },
	{ 0xc5850110, "printk" },
	{ 0xf67c3cc1, "gpiod_get_raw_value" },
	{ 0x4fa3ac45, "gpiod_set_raw_value" },
	{ 0xbc973228, "gpio_to_desc" },
	{ 0xb1ad28e0, "__gnu_mcount_nc" },
};

MODULE_INFO(depends, "");


MODULE_INFO(srcversion, "04B93F5E45435FA06D078E3");
