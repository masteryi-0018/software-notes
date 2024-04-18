## 环境

> 下载`.NET`框架（里面包含了framework和其他的东西）
> 
> 下面还有专门的framework，以及编码包下载

.Net的编程语言，默认安装在`C:\Windows\Microsoft.NET`，没有机会自定义安装目录


## 2种方式

1. dotnet new console
后续版本的.NET SDK推荐创建项目的方式，也就是直接使用dotnet命令

2. csc
对于单个文件的编译一般用不到项目，直接使用其编译器就可以完成。但是一般找不到这个命令，所以需要添加环境变量：

```sh
C:\Windows\Microsoft.NET\Framework64\v4.0.30319
```


## 命令

```sh
csc .\test.cs
.\test.exe
```