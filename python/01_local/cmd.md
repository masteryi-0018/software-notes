## python包发布（一）

> cpp使用cmake等工具编译出二进制文件，连同头文件作为release，那py呢？

## 直接使用：作为脚本使用

1. 一个文件，只涉及工作目录

工作目录： 一直都是执行命令的地方，决定创建文件，读取文件时候的根目录

```sh
# 一般在文件所在位置
python core.py
core.py loaded
当前工作目录: /home/gy/proj/software-notes/python/01_local/hello_pkg
当前搜索路径: /home/gy/proj/software-notes/python/01_local/hello_pkg
当前模块: __main__
当前包: None


# 也可以不在
python hello_pkg/core.py
core.py loaded
当前工作目录: /home/gy/proj/software-notes/python/01_local
当前搜索路径: /home/gy/proj/software-notes/python/01_local/hello_pkg
当前模块: __main__
当前包: None
```

2. 多个文件

搜索路径：决定import的时候去哪里找模块
1. python api.py或者python hello_pkg/api.py，也就是以文件运行，sys的搜索路径就是文件所在目录
2. python -m hello_pkg.api，也就是以模块的身份运行，sys的搜索路径就是执行命令的地方，这里最好是包所在的目录

```sh
# 这时候被import的文件会执行一次，比如core.py会打印core.py loaded
# 会出现__pycache__的缓存
python hello_pkg/api.py
api.py loaded
当前工作目录: /home/gy/proj/software-notes/python/01_local
当前搜索路径: /home/gy/proj/software-notes/python/01_local/hello_pkg
当前模块: __main__
当前包: None
core.py loaded
当前工作目录: /home/gy/proj/software-notes/python/01_local
当前搜索路径: /home/gy/proj/software-notes/python/01_local/hello_pkg
当前模块: core
当前包:
Hello, core

python api.py
api.py loaded
当前工作目录: /home/gy/proj/software-notes/python/01_local/hello_pkg
当前搜索路径: /home/gy/proj/software-notes/python/01_local/hello_pkg
当前模块: __main__
当前包: None
core.py loaded
当前工作目录: /home/gy/proj/software-notes/python/01_local/hello_pkg
当前搜索路径: /home/gy/proj/software-notes/python/01_local/hello_pkg
当前模块: core
当前包:
Hello, core

# 以模块运行
python -m api
api.py loaded
当前工作目录: /home/gy/proj/software-notes/python/01_local/hello_pkg
当前搜索路径: /home/gy/proj/software-notes/python/01_local/hello_pkg
当前模块: __main__
当前包:
core.py loaded
当前工作目录: /home/gy/proj/software-notes/python/01_local/hello_pkg
当前搜索路径: /home/gy/proj/software-notes/python/01_local/hello_pkg
当前模块: core
当前包:
Hello, core

python -m hello_pkg.api
api.py loaded
当前工作目录: /home/gy/proj/software-notes/python/01_local
当前搜索路径: /home/gy/proj/software-notes/python/01_local
当前模块: __main__
当前包: hello_pkg
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/home/gy/proj/software-notes/python/01_local/hello_pkg/api.py", line 19, in <module>
    import core
ModuleNotFoundError: No module named 'core'
# 这里如果修改为 import hello_pkg.core 就可以了，因为搜索路径 01_local 下面没有 core
```

报的层级：影响相对导入时的 . 和 .. 代表的含义
1. python -m hello_pkg.hello_subpkg.hello，当前包是hello_subpkg，所以..代表了hello_pkg，有父包
2. python -m hello_subpkg.hello，当前包是hello_subpkg，没有父包，所以..会beyond top-level package

```sh
python -m hello_pkg.hello_subpkg.hello
hello.py loaded
当前工作目录: /home/gy/proj/software-notes/python/01_local
当前搜索路径: /home/gy/proj/software-notes/python/01_local
当前模块: __main__
当前包: hello_pkg.hello_subpkg
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/home/gy/proj/software-notes/python/01_local/hello_pkg/hello_subpkg/hello.py", line 19, in <module>
    import core
ModuleNotFoundError: No module named 'core'

# 修改为 from .. import core 就可以，因为 .. 代表了 hello_pkg.hello_subpkg 的上级包，也就是 hello_pkg
# 当然 import hello_pkg.core，from hello_pkg import core 一定是可以的
python -m hello_pkg.hello_subpkg.hello
hello.py loaded
当前工作目录: /home/gy/proj/software-notes/python/01_local
当前搜索路径: /home/gy/proj/software-notes/python/01_local
当前模块: __main__
当前包: hello_pkg.hello_subpkg
core.py loaded
当前工作目录: /home/gy/proj/software-notes/python/01_local
当前搜索路径: /home/gy/proj/software-notes/python/01_local
当前模块: hello_pkg.core
当前包: hello_pkg

# 没有父包，报错
python -m hello_subpkg.hello
hello.py loaded
当前工作目录: /home/gy/proj/software-notes/python/01_local/hello_pkg
当前搜索路径: /home/gy/proj/software-notes/python/01_local/hello_pkg
当前模块: __main__
当前包: hello_subpkg
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/home/gy/proj/software-notes/python/01_local/hello_pkg/hello_subpkg/hello.py", line 25, in <module>
    from .. import core
ImportError: attempted relative import beyond top-level package
```


## 打包发布：作为包使用

如果没按照包的形式组织代码的import，那么在test.py使用的时候，就会有很多麻烦：

```sh
python test.py
test.py loaded
api.py loaded
当前工作目录: /home/gy/proj/software-notes/python/01_local
当前搜索路径: /home/gy/proj/software-notes/python/01_local
当前模块: hello_pkg.api
当前包: hello_pkg
Traceback (most recent call last):
  File "/home/gy/proj/software-notes/python/01_local/test.py", line 4, in <module>
    import hello_pkg.api
  File "/home/gy/proj/software-notes/python/01_local/hello_pkg/api.py", line 19, in <module>
    import core
ModuleNotFoundError: No module named 'core'
```

所以如果代码要给别人使用，最好是根据包来组织结构
