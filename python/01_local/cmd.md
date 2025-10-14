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

打包之前，自己测试发现

1. 在hello.py中导入core.py会报错：ImportError: attempted relative import beyond top-level package

因为这不是一个包，只是自己的项目代码，所以不能从父目录导入；这里就强烈推荐使用统一的导入的流程，也就是从顶层包开始导入，例如：
- import hello_pkg.core
- from hello_pkg import core

这里有点类似cpp中的头文件，成熟的项目也会从一个固定统一的目录导入

2. 在测试文件test.py中，要想使用这个包中的东西，导入api后，api导入core的逻辑就和此时的位置有关系，会显示：ModuleNotFoundError: No module named 'core'

所以如果python代码已经有了目录结构，最好就按照项目的导入来搞