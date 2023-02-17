# 树莓派 Ubuntu Server 系统下启用 spi 用户组,实现用户使用 spi 相关 GPIO

> 设备: 树莓派 3b+
>
> 系统: [Ubuntu Server](https://ubuntu.com/download/raspberry-pi)
>
> 内核: Linux raspberrypi 5.4.0-1059-raspi #67-Ubuntu SMP PREEMPT aarch64 GNU/Linux
>
> 环境: python3 + luma spi 库
>

## 权限获取

### 启用 spi

> 不启用 spi 可跳过

#### 方法1

直接在 /boot/firmware/usercfg.txt 内添加 `dtparam=spi=on` 即可

#### 方法2

Ubuntu Server 可以安装 raspi-config，参考 [1.安装树莓派配置工具raspi-config (yahboom.com)](https://www.yahboom.com/build.html?id=4532&cid=443)

再根据官方系统教程在 `sudo raspi-config` 下开启 spi 即可

### 添加用户组

> 不同于原生 rpios, Ubuntu Server 默认不带有 gpio 和 spi 用户组。
>
> 本项目参考 [RPI.GPIO](https://sourceforge.net/projects/raspberry-gpio-python/files/) 模块内自带的 `create_gpio_user_permissions.py` 脚本，
>
> 结合 [官方 os](https://www.raspberrypi.com/software/) 内 `/etc/udev/rules.d/com.rules` 文件, 完成了 spi 用户权限的补全脚本

sudo 运行如下脚本
```bash
sed -i "s/yourname/$USER/g" get_user_permissions/create_gpio_user_permissions.py
sed -i "s/yourname/$USER/g" get_user_permissions/create_spi_user_permissions.py
sudo get_user_permissions/create_gpio_user_permissions.py
sudo get_user_permissions/create_spi_user_permissions.py
```

如想手动修改文件, 请自行参考脚本与官方系统文件

## todo

- [ ] 添加 I2C 权限脚本
