"""
Decorators let you add extra behavior to a function, without changing the function's code.
A decorator is a function that takes another function as input and returns a new function.
"""


def my_decorator(func):
    def tea():
        print("Boil Water")
        print(func().upper())
        print("Add Sugar and tea powder")
        print("Add Milk")

    return tea


@my_decorator
def add_extra_steps():
    # print("Add Ginger")
    # print("Add Masala")
    return "Add Ginger"


# add_extra_steps()


# Decorator With Arguments
# Decorators can accept their own arguments by adding another wrapper level.
def api_view(method):
    print("api_view is called")
    def api_method(func):
        print("api_method is called")
        def api():
            func()
            if method == "POST":
                print("This is a POST API")
            elif method == "GET":
                print("This is a GET API")

        return api

    return api_method


@api_view("POST")
def login():
    print("Login Function Called")
    return None


login()
