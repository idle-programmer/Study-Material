mylist = ["apple", "banana", "cherry"]

# Accessing by index, negative index and by range
# check item using "in" operator
# change item value using index or by range

mylist.insert(2, "watermelon")  # add item using insert() at given index

# Add item to the end using append()
# add two list or (list+tuple) using extend() or by using "+"
mylist.extend(mylist)

# remove specfic item using remove()
# remove item with specfic index using pop() else remove last element with pop
# Use del keyword to delete a list
# Use clear() to empty a list


# List Comprehension
# newlist = [expression for item in iterable if condition == True]

# Sort current list using sort(), sort(reverse = True) for reverse

# List Copy
mylist2 = mylist.copy()  # shallow copy
mylist3 = list(mylist2)
mylist4 = mylist3[:]
import copy

mylist5 = copy.deepcopy(mylist4)  # deep copy
