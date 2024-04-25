## 环境

> Windows下使用MSVC或者GCC（通过mingw）


## 命令

### GCC
使用gcc（通过mingw）
```sh
# 不加参数，输出a.exe
g++ .\test.cpp
.\a.exe

# 加参数，指定产物名字
g++ .\test.cpp -o test
.\test.exe
```

程序 g++ 是将 gcc 默认语言设为 C++ 的一个特殊的版本，链接时它自动使用 C++ 标准库而不用 C 标准库。通过遵循源码的命名规范并指定对应库的名字，用 gcc 来编译链接 C++ 程序是可行的。

### MSVC
使用MSVC，只能通过微软的命令行进去，cd到目录下操作；官方不推荐自己添加环境变量，我试了一下找不到标准库
```sh
cl /EHsc test.cpp
.\test.exe
```

这里`/EHsc` 命令行选项指示编译器启用标准 C++ 异常处理行为。如果没有它，则引发的异常可能导致未受损对象和资源泄漏。这个命令会产生.obj文件。

### clang

说起clang，就会联想到llvm，这2个概念的关系，其实是clang作为`编译器前端`，将类C语言接入到llvm的后端上，后面的事情由llvm编译为机器码。而llvm是一个很大的编译器项目，其他语言不需要clang这样的工具也可以直接使用llvm进行编译。

网上查询一些博客，发现其实clang没有提供c/c++的标准库，本质上需要借用msvc或者gnu的标准库，所以需要主动配置。msvc就不提了，经过上面的验证，只能在VS的powershell中运行clang，而因为我之前已经将mingw/bin添加到了环境中，所以我猜测我的clang直接寻找了mingw的标准库，所以可以顺利编译通过。

clang++和clang，就像g++和gcc的关系。

相关链接：
- clang+llvm官网：<https://clang.llvm.org/>
- llvm官网：<https://www.llvm.org/>
- github：<https://github.com/llvm/llvm-project>
- 参考：<https://alibabatech.medium.com/gcc-vs-clang-llvm-an-in-depth-comparison-of-c-c-compilers-899ede2be378>
- 参考：<https://www.cnblogs.com/RioTian/p/17758813.html>
- 参考：<https://zhuanlan.zhihu.com/p/380290758>