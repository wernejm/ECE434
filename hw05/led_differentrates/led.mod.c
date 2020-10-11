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
	{ 0xbed3e003, "param_ops_uint" },
	{ 0xfe990052, "gpio_free" },
	{ 0x58d1f292, "gpiod_unexport" },
	{ 0xc8d167d5, "kthread_stop" },
	{ 0xa15e4390, "wake_up_process" },
	{ 0x6d48ef8b, "kthread_create_on_node" },
	{ 0x3349566e, "gpiod_export" },
	{ 0x2308e66c, "gpiod_direction_output_raw" },
	{ 0x47229b5c, "gpio_request" },
	{ 0xcada8fbe, "kobject_put" },
	{ 0x2f56235b, "sysfs_create_group" },
	{ 0x49453c41, "kobject_create_and_add" },
	{ 0x52856538, "kernel_kobj" },
	{ 0x3c3ff9fd, "sprintf" },
	{ 0x86332725, "__stack_chk_fail" },
	{ 0xbcab6ee6, "sscanf" },
	{ 0x8f678b07, "__stack_chk_guard" },
	{ 0x84b183ae, "strncmp" },
	{ 0xefd6cf06, "__aeabi_unwind_cpp_pr0" },
	{ 0xf9a482f9, "msleep" },
	{ 0x4fa3ac45, "gpiod_set_raw_value" },
	{ 0xbc973228, "gpio_to_desc" },
	{ 0xb3f7646e, "kthread_should_stop" },
	{ 0xc5850110, "printk" },
	{ 0xb1ad28e0, "__gnu_mcount_nc" },
};

MODULE_INFO(depends, "");


MODULE_INFO(srcversion, "1A80B1575B34D8640FA077D");
