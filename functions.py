# Function
def add_one(number):
    return number + 1


# First Class Objects
def say_hello(name):
    return f"Hello {name}"


def be_awesome(name):
    return f"Yo {name}, together we are the awesome!"


def greet_bob(greeter_func):
    return greeter_func("Bob")


# Inner Functions
def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")

    second_child()
    first_child()


# Returning Functions From Functions
def second_parent(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"

    if num == 1:
        return first_child
    else:
        return second_child


if __name__ == '__main__':
    print(add_one(2))
    print(greet_bob(say_hello))
    print(greet_bob(be_awesome))
    parent()
    first = second_parent(1)
    second = second_parent(2)
