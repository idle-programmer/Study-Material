# Parameters vs Arguments
def my_function(name):  # name is a parameter
    print("Hello", name)


my_function("Emil")  # "Emil" is an argument

"""
Keyword Arguement and Positional Arguement
my_function(fname, lname) , this is Positional Arguement
my_function(name = "friend"), this is Keyword Arguement
"""


"""
You can specify that a function can have ONLY positional arguments. To specify positional-only arguments, add , / after the arguments:
def my_function(name, /)
"""

"""
To specify that a function can have only keyword arguments, add *, before the arguments:
def my_function(*, name)
"""

"""
You can combine both argument types in the same function. Arguments before / are positional-only, and arguments after * are keyword-only:
def my_function(a, b, /, *, c, d)
my_function(5, 10, c = 15, d = 20)
"""

# Arbitrary Arguments - *args
"""The *args parameter allows a function to accept any number of positional arguments.
Inside the function, args becomes a tuple containing all the passed arguments:"""

"""Arbitrary Keyword Arguments - **kwargs
If you do not know how many keyword arguments will be passed into your function, add two asterisks ** before the parameter name.
This way, the function will receive a dictionary of arguments and can access the items accordingly:"""
