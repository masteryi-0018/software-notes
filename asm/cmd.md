## 环境

> linux下，nasm，ld
>
> sudo apt install nasm


## 命令

```sh
nasm -f elf test.asm -o test.o
ld -m elf_i386 test.o -o test
```


## 其他

上述命令是32位系统的，如果需要编译64位的版本，需要将`-f`和`-m`同时替换。例如：

```sh
nasm -f elf64 test.asm -o test.o
ld -m elf_x86_64 test.o -o test
```