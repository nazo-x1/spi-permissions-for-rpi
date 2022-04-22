import grp
import subprocess

def ensure_gpiogroup():
    try:
        grp.getgrnam('gpio')
    except KeyError:
        print('GPIO group does not exist - creating...')
        subprocess.call(['groupadd', '-f', '-r', 'gpio'])
        subprocess.call(['adduser', 'yourname', 'gpio'])
        # in future, also for groups:
        #   spi
        #   i2c
        add_udev_rules()

def add_udev_rules():
    with open('/etc/udev/rules.d/99-gpio.rules','w') as f:
        f.write("""SUBSYSTEM=="bcm2835-gpiomem", GROUP="gpio", MODE="0660"
SUBSYSTEM=="gpio", GROUP="gpio", MODE="0660"
SUBSYSTEM=="gpio", KERNEL=="gpiochip*", ACTION=="add", PROGRAM="/bin/sh -c 'chgrp -R gpio /sys/class/gpio && chmod -R g=u /sys/class/gpio'"
SUBSYSTEM=="gpio", ACTION=="add", PROGRAM="/bin/sh -c 'chgrp -R gpio /sys%p && chmod -R g=u /sys%p'"
SUBSYSTEM=="pwm", ACTION!="remove", PROGRAM="/bin/sh -c 'chgrp -R gpio /sys%p && chmod -R g=u /sys%p'"
""")

if __name__ == '__main__':
    ensure_gpiogroup()
