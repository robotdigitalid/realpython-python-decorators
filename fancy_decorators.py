import functools

from example import debug, timer
from simple_decorators import do_twice4 as do_twice
from dataclasses import dataclass


# Decorating Classes
class TimeWaster:
    @debug
    def __init__(self, max_num):
        self.max_num = max_num

    @timer
    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([i**2 for i in range(self.max_num)])


# Decorate The Whole Class
@dataclass
class PlayingCard:
    rank: str
    suit: str


@timer
class TimeWaster2:
    def __init__(self, max_num):
        self.max_num = max_num

    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([i**2 for i in range(self.max_num)])


# Nesting Decorators
@debug
@do_twice
def greet(name):
    print(f"Hello {name}")


@do_twice
@debug
def greet2(name):
    print(f"Hello {name}")


# Decorators With Arguments
def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat
    return decorator_repeat


@repeat(num_times=4)
def greet3(name):
    print(f"Hello {name}")


# Both Flexible Decorators With Or Without Arguments
def repeat2(_func=None, *, num_times=2):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat

    if _func is None:
        return decorator_repeat
    else:
        return decorator_repeat(_func)


@repeat2
def say_whee():
    print("Whee!")


@repeat2(num_times=3)
def greet4(name):
    print(f"Hello {name}")


# Stateful Decorators
def count_calls(func):
    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.num_calls += 1
        print(f"Call {wrapper_count_calls.num_calls} of {func.__name__!r}")
        return func(*args, **kwargs)
    wrapper_count_calls.num_calls = 0
    return wrapper_count_calls


@count_calls
def say_whee2():
    print("Whee!")


# Classes As Decorators
class Counter:
    def __init__(self, start=0):
        self.count = start

    def __call__(self):
        self.count += 1
        print(f"Current count is {self.count}")


class CountCalls:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*args, **kwargs)


@CountCalls
def say_whee3():
    print("Whee!")


if __name__ == '__main__':
    tw = TimeWaster(1000)
    tw.waste_time(999)
    tw2 = TimeWaster2(1000)
    tw.waste_time(999)
    greet("Eva")
    greet2("Eva")
    greet3("World")
    say_whee()
    greet4("Penny")
    say_whee2()
    say_whee2()
    print(say_whee2.num_calls)
    counter = Counter()
    counter()
    counter()
    print(counter.count)
    say_whee3()
    say_whee3()
    print(say_whee3.num_calls)
