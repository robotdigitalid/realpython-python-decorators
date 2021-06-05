# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from simple_decorators import do_twice, do_twice2


@do_twice2
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


@do_twice
def say_whee():
    print("Whee!")


# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    print_hi('PyCharm')
    say_whee()
    print(...)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
