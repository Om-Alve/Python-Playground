# Challenge : Print "Decorated" before hello world without changing the fun function's body


def decorator(original):
    def wrapper():
        print("Decorated")
        return original()
    return wrapper


# fun = decorator(fun)
@decorator
def fun():
    print("Hello World")


fun()
