print("core.py loaded")

import os

# 执行命令位置
current_working_directory = os.getcwd()
print("当前工作目录:", current_working_directory)

# 文件所在目录
script_path = os.path.abspath(__file__)
script_directory = os.path.dirname(script_path)
# print("脚本文件路径:", script_path)
print("脚本所在目录:", script_directory)

def say_hello(name="World"):
    return f"Hello, {name}!"

# 只会在执行当前文件时运行，被导入时不会运行
if __name__ == "__main__":
    print(say_hello())