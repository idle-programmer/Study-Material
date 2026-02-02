mytuple = ("apple", "banana", "cherry")

# Accessing by index, negative index and by range
# check item using "in" operator

# Change Tuple Values:
# Convert the tuple into a list, change the list, and convert the list back into a tuple.
# do not have a built-in append(), Convert the tuple into a list and add element
# Add tuple to tuple by "+"
# Remove element by Convert the tuple into a list and remove() element
# del to delete tuple

# Unpacking Tuple
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(red)  # prints a list of elements
# count()
# index()


# how does tupple stores data?
"""
Tuples store references to objects in a fixed-size array of object pointers, 
similar to lists, but are immutable—meaning their references can't be changed or resized.
"""

"""
A tuple can store different data types, but it is immutable, 
so its elements cannot be changed once created. However, 
mutable objects inside a tuple can be modified.
"""

