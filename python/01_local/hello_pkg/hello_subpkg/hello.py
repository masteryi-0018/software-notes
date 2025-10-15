print("hello.py loaded")

import os
current_working_directory = os.getcwd()
print("当前工作目录:", current_working_directory)

import sys
print("当前搜索路径:", sys.path[0])

print("当前模块:", __name__)

print("当前包:", __package__)


def say_hello():
    print(f"Hello, hello")


import core
# from .. import core

# import hello_pkg.core
# from hello_pkg import core