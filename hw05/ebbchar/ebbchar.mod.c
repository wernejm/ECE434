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
	{ 0x1b679bd6, "class_unregister" },
	{ 0x85b15422, "device_destroy" },
	{ 0x538394b2, "class_destroy" },
	{ 0x9747b149, "device_create" },
	{ 0x6bc3fbc0, "__unregister_chrdev" },
	{ 0xc5258d24, "__class_create" },
	{ 0x59f3ae4, "__register_chrdev" },
	{ 0x51a910c0, "arm_copy_to_user" },
	{ 0xefd6cf06, "__aeabi_unwind_cpp_pr0" },
	{ 0x5f754e5a, "memset" },
	{ 0x2cfde9a2, "warn_slowpath_fmt" },
	{ 0xcbd4898c, "fortify_panic" },
	{ 0xd9ce8f0c, "strnlen" },
	{ 0xae353d77, "arm_copy_from_user" },
	{ 0x88db9f48, "__check_object_size" },
	{ 0x2e5810c6, "__aeabi_unwind_cpp_pr1" },
	{ 0xc5850110, "printk" },
	{ 0xb1ad28e0, "__gnu_mcount_nc" },
};

MODULE_INFO(depends, "");


MODULE_INFO(srcversion, "1FCFF9547BED129ED2C244B");
