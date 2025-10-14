print("test.py loaded")

# import hello_pkg.api
# from hello_pkg import api

# print(hello_pkg.api.say_hello("Test"))
# print(api.say_hello("Test"))

def say_test(name="Test"):
    print(f'Hello, {name}')


if __name__ == "__main__":
    say_test()