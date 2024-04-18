## 环境

> 需要依赖JDK的环境，或者nodejs环境
>
> 一般建议IDEA或者AS的IDE，命令行的话需要下载编译器
>
> 早期和当前的版本，有区别


基于java，Kotlin 可以编译成Java字节码，也可以编译成 JavaScript，方便在没有 JVM 的设备上运行。

在GitHub的release下载环境：
- 早期：<https://github.com/JetBrains/kotlin/releases/tag/v1.1.2-2>
- 当前：<https://github.com/JetBrains/kotlin/releases/tag/v2.0.0-RC1>


## 命令

编译为java：
```sh
# 1. 早期版本
# 进入交互式
kotlinc
kotlinc-jvm

# 编译，运行
kotlinc test.kt -include-runtime -d test.jar
java -jar test.jar

# 2. 当前版本（不太会使用）
konanc
kotlinc-native
```

编译为js：（没成功）
```sh
kotlinc-js test.kts -output test.js
node test.ks
```


## 笔记

- vscode依旧不支持语法高亮
- 总的来说使用命令行不使用IDE有一定难度