## 环境

> 有2种下载的方式，带有工具链和不带有工具链的
>
> <https://rubyinstaller.org/downloads/>
>
> 工具链是指：它提供了最大数量的兼容 gem，并与 Ruby 一起安装 MSYS2 Devkit，因此可以立即编译带有 C 扩展名的 gem
>
> 默认是为当前用户安装，环境变量在用户的path中创建


## 命令

```sh
# 解释器
ruby .\test.rb

# 交互式
irb
```


## 其他

第一次运行完安装包后会打开一个终端，选择msys2的安装，这里我本地已经有了msys2和mingw，好像是重复安装了的样子，最后点击回车退出就好

```sh
   1 - MSYS2 base installation
   2 - MSYS2 system update (optional)
   3 - MSYS2 and MINGW development toolchain
```