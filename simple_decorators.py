import functools
from datetime import datetime


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


def say_whee1():
    print("Whee!")


say_whee1 = my_decorator(say_whee1)


def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass  # Hush, the neighbors are asleep
    return wrapper


def say_whee2():
    print("Whee!")


say_whee2 = not_during_the_night(say_whee2)


# Pie Syntax
@my_decorator
def say_whee3():
    print("Whee!")


# Reusing Decorators
def do_twice(func):
    def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice


# Decorating Functions With Arguments
def do_twice2(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice


# Returning Values From Decorated Functions


def do_twice3(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice


@do_twice3
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"


hi_adam = return_greeting("Adam")


def do_twice4(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice


if __name__ == '__main__':
    say_whee1()
    say_whee2()
    print(hi_adam)
