Class
def decorator(func):
    def wrapper():
        print("This will be executed first")
        func()
        print("This will be executed at last")

        return wrapper

@decorator
def func():
    print("This will be executed second")

