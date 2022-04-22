import grp
import subprocess

def ensure_spigroup():
    try:
        grp.getgrnam('spi')
    except KeyError:
        print('SPI group does not exist - creating...')
        subprocess.call(['groupadd', '-f', '-r', 'spi'])
        subprocess.call(['adduser', 'yourname', 'spi'])
        # in future, also for groups:
        #   i2c
        add_udev_rules()

def add_udev_rules():
    with open('/etc/udev/rules.d/99-spi.rules','w') as f:
        f.write("""SUBSYSTEM=="spidev", GROUP="spi", MODE="0660"
""")

if __name__ == '__main__':
    ensure_spigroup()
