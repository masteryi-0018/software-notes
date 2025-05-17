## 环境

> cpp异常处理和断言，g++编译


## 命令

### 异常
```sh
# 默认开启异常
g++ -o test test.cpp

# 手动关闭异常
g++ -fno-exceptions -o test test.cpp
```

如果没有开启编译选项但使用了异常，会报错：`exception handling disabled, use ‘-fexceptions’ to enable`

当使用 -fno-exceptions 时：
1. try, catch 和 throw 关键字将无法使用
2. 标准库也不会抛出异常
3. 代码会变得更小更快，但需要其他错误处理机制

### 断言
```sh
# 调试模式默认开启断言
g++ -o test test.cpp

# 发布版本关闭
g++ -o test test.cpp -DNDEBUG
```

- 用于捕捉程序中的逻辑错误
- 仅在调试阶段有效
- 失败时直接终止程序Aborted (core dumped)