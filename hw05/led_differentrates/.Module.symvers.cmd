cmd_/home/debian/ECE434_repo/hw05/led_differentrates/Module.symvers := sed 's/ko$$/o/' /home/debian/ECE434_repo/hw05/led_differentrates/modules.order | scripts/mod/modpost -m    -o /home/debian/ECE434_repo/hw05/led_differentrates/Module.symvers -e -i Module.symvers   -T -