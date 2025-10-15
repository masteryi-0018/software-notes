## python 包发布（二）

> cpp 使用 cmake 等工具编译出二进制文件，连同头文件作为 release，那 py 呢？

## 打包发布：作为包使用（接 01_local）

那么这里的 import 关系全部使用绝对导入，从包名开始

现在本地已经可以用 test 使用起来了，但是如果别人使用，还是要把 hello_pkg 的文件夹发给别人，所以这时候打包和安装就出现了

| 打包/构建                   | 安装             | 备注                                       |
| --------------------------- | ---------------- | ------------------------------------------ |
| python setup.py sdist       |                  | dist/tar.gz                                |
| python setup.py bdist       |                  | dist/tar.gz, 有 build 目录                 |
| python setup.py bdist_wheel |                  | dist/whl, 有 build 目录                    |
| python setup.py install     |                  | dist/egg, 有 build 目录，带有安装          |
| ==                          | ==               | ==                                         |
|                             | pip install .    | 构建+安装，顺序是 pyproject.toml->setup.py |
| ==                          | pip install -e . | 是以链接方式安装，适合调试                 |
| ==                          | ==               | ==                                         |
| python -m build             | ==               | 只构建，生成 dist/tar.gz 和 dist/whl       |
|                             |                  | 顺序是 pyproject.toml->setup.py            |
