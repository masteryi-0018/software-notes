print("core.py loaded")

import os
current_working_directory = os.getcwd()
print("当前工作目录:", current_working_directory)

import sys
print("当前搜索路径:", sys.path[0])

print("当前模块:", __name__)

print("当前包:", __package__)


def say_core():
    print(f"Hello, core")


from hello_pkg.hello_subpkg import hello
hello.say_hello()