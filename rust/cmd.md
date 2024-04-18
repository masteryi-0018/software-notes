## 环境

> Rust 的编译工具依赖 C 语言的编译工具
>
> 默认依赖msvc，如果自己有mingw的环境也可以


## 命令

```sh
# 单个文件
rustc .\test.rs
.\test.exe

# 项目
cargo new hello
cd .\hello
cargo build # 可选，可以直接run
cargo run
```


## 笔记

- 包管理器：cargo
- 安装工具下载的慢，之后安装时下载依赖也慢，体验不好
- 最好是提前下载好msvc，如果是gnu的，需要自定义安装
- 编译中会生成.pdb的文件