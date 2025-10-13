## python包发布

> cpp使用cmake等工具编译出二进制文件，连同头文件作为release，那py呢？

## 直接使用

1. 一个文件
在哪里使用一般不重要

```sh
# 一般在文件所在位置
python core.py
当前工作目录: /home/gy/proj/software-notes/python/release/hello_pkg
脚本所在目录: /home/gy/proj/software-notes/python/release/hello_pkg

# 也可以不在
python hello_pkg/core.py
当前工作目录: /home/gy/proj/software-notes/python/release
脚本所在目录: /home/gy/proj/software-notes/python/release/hello_pkg
```

2. 多个文件
```sh
python hello_pkg/api.py
# 这时候被import的文件会执行一次，比如core.py会打印core.py loaded
# 会出现__pycache__的缓存
```

## 打包


```sh

```