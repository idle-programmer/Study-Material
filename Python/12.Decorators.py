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

# Interview Questions

# Can a function has multiple decorators, if yes then how they are executed by order?
""" Yes, A function can have multiple decorators. They are applied from 
the innermost (closest to the function) to the outermost."""

# What are the advantages of using decorators in Python, and what happens if we don't use them?
"""
Decorators in Python allow us to add extra behavior like logging, caching, authentication, or 
validation to a function without modifying its original code.
Advantages:
Reusability – write logic once, apply everywhere
Separation of concerns – keeps business logic clean
Cleaner and more readable syntax using @decorator
Easy to maintain and scale

If we don’t use decorators, we’d have to repeat the same boilerplate code inside multiple 
functions, which makes the code messy and harder to maintain.

Example:
@lru_cache for caching or @app.route in Flask.
Also, we use functools.wraps to preserve the original function’s metadata.
"""