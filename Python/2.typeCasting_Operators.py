int()
float()
str()
list()
set()
dict()
tuple()
bool()
complex()

# Interview Questions
# implicit vs explicit type conversion with examples
"""
explicit : done by us, eg: int("3")
implicit : done by python, eg: *args is tupple, **args is dict.
"""

# many values that evaluate to False
bool(False)  # return False
bool(None)  # return False
bool(0)  # return False
bool("")  # return False
bool(())  # return False
bool([])  # return False
bool({})  # return False

# Operators
# Arithmetic: +, -, *, /, %, **, //
# Logical: and, or, not
# Identity: is, is not

# What is membership Operators?
"""
in 
not in
"""
# Difference b/w is & ==?
"""
is checks if two variables point to the same object in memory (identity comparison).
== checks if the values of two objects are equal (equality comparison).
"""

# Write a python program to add two numbers without using + operator
def add(a,b):
    while b!=0:
        c=a&b
        a=a^b
        b=c<<1
    return a

print(add(2,3))