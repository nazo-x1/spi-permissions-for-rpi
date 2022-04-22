# 获取树莓派 Ubuntu Server spi 权限

> 设备: 树莓派 3b+
>
> 系统: [Ubuntu Server](https://ubuntu.com/download/raspberry-pi)
>
> 内核: Linux raspberrypi 5.4.0-1059-raspi #67-Ubuntu SMP PREEMPT aarch64 GNU/Linux
>
> 环境: python3
>

## 权限获取

> 不同于原生 rpios, Ubuntu Server 默认不带有 gpio 和 spi 用户组。
>
> 本项目参考 [RPI.GPIO](https://sourceforge.net/projects/raspberry-gpio-python/files/) 模块内自带的 `create_gpio_user_permissions.py` 脚本，
>
> 结合 [官方 os](https://www.raspberrypi.com/software/) 内 `/etc/udev/rules.d/com.rules` 文件, 完成了 spi 用户权限的补全脚本

sudo 运行如下脚本即可
```bash
sed -i "s/yourname/$USER/g" get_user_permissions/create_gpio_user_permissions.py
sed -i "s/yourname/$USER/g" get_user_permissions/create_spi_user_permissions.py
sudo get_user_permissions/create_gpio_user_permissions.py
sudo get_user_permissions/create_spi_user_permissions.py
```

如想手动修改文件, 请自行参考脚本与官方系统文件

## todo

- [ ] 添加 I2C 权限脚本