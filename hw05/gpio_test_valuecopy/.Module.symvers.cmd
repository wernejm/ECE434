cmd_/home/debian/exploringBB/extras/kernel/gpio_test/Module.symvers := sed 's/ko$$/o/' /home/debian/exploringBB/extras/kernel/gpio_test/modules.order | scripts/mod/modpost -m    -o /home/debian/exploringBB/extras/kernel/gpio_test/Module.symvers -e -i Module.symvers   -T -
