print("api.py loaded")

import core

def say_api(name="Api"):
    print(f'Hello, {name}')
    core.say_hello(name)


if __name__ == "__main__":
    say_api()