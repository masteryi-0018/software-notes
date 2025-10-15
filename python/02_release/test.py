print("test.py loaded")

import hello_pkg
import hello_pkg.api
# from hello_pkg import api

hello_pkg.api.say_api()
# api.say_api()

def say_test():
    print(f'Hello, test')


if __name__ == "__main__":
    say_test()