## 环境

> linux下，g++，ld


## 命令

```sh
# step
cpp add.cc add.i
/usr/lib/gcc/x86_64-linux-gnu/9/cc1 add.i
as add.s -o add.o

# g++ step
g++ -E add.cc -o add.i
g++ -S add.i -o add.s
g++ -c add.s -o add.o

# lib
ar rsc libadd.a add.o
g++ --shared -o libadd.so add.o
```