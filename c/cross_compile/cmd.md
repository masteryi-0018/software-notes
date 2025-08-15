## 环境

> Windows或者WSL，安装交叉编译工具链就可以

用qemu的时候要加静态链接，否则会依赖系统动态库。这个流程同样适用于arm架构。

## 命令

```sh
sudo apt install gcc-riscv64-linux-gnu

riscv64-linux-gnu-gcc test.c -o test -static

sudo apt install qemu-user qemu-user-static

qemu-riscv64 test
```