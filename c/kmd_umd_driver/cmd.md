## 环境

> 虚拟机安装的linux环境，不能是WSL，因为WSL是2微软定制内核，无法开发内核

虚拟机可以用virtual box或者VM ware work station

## 命令

```sh
make

sudo insmod mychardev.ko

sudo dmesg | grep mychardev   # 查看注册的 major 号，比如 240
sudo mknod /dev/mychardev c 240 0
sudo chmod 666 /dev/mychardev

gcc test_user.c -o test_user
./test_user

sudo dmesg | tail

sudo rmmod mychardev
```