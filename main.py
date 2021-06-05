# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from function import add_one, greet_bob, say_hello, be_awesome, parent, second_parent


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print(add_one(2))
    print(greet_bob(say_hello))
    print(greet_bob(be_awesome))
    parent()
    first = second_parent(1)
    second = second_parent(2)
    print(first())
    print(second())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
