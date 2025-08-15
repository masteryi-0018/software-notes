## 环境

> 虚拟机安装的linux环境，不能是WSL，因为WSL是2微软定制内核，无法开发内核

虚拟机可以用virtual box或者VM ware work station

## 命令

```sh
make

sudo insmod hello_driver.ko

sudo dmesg | tail

sudo rmmod hello_driver

sudo dmesg | tail
```