print("api.py loaded")

import os
current_working_directory = os.getcwd()
print("当前工作目录:", current_working_directory)

import sys
print("当前搜索路径:", sys.path[0])

print("当前模块:", __name__)

print("当前包:", __package__)


def say_api():
    print(f"Hello, api")


# import core
# core.say_core()

# import hello_pkg.core
# hello_pkg.core.say_core()

from hello_pkg import core
core.say_core()