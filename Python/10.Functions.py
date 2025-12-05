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


# Function Variable scope
# A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.
# As explained in the example above, the variable x is not available outside the function, but it is available for any function inside the function:
def myfunc():
    x = 300

    def myinnerfunc():
        print(x)

    myinnerfunc()


myfunc()

# map() function
"""
Take every item in a list, do something to it, and give me the new list.
Syntax idea: map(function, iterable)
It does: applies the function to each element, one by one.
"""

new_prices = list(map(lambda p: p + 10, [100, 200, 300]))
convert_to_int = list(map(int, ["2", "4", "6"]))
print(new_prices, convert_to_int)


# filter() function
"""
Keep only the items that pass a test.
Idea: filter = select.
It checks every element in a list with a function.
If the function returns True, the element is kept; if False, it is removed.
"""
adults = list(filter(lambda age: age >= 18, [12, 17, 18, 21, 15, 30]))
print(adults)


# reduce() function
"""
Combine all items into ONE final result.
Idea: reduce = fold/combine.
It takes a list and keeps combining pairs until only one value remains.
Needs from functools import reduce first.
"""
from functools import reduce

total = reduce(lambda x, y: x + y, [100, 200, 300])
print(total)  # 600


# Recursion
# Recursion is when a function calls itself.
