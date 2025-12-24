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

# Interview Question
# Diffn b/w remove() & del
"""
remove() deletes an item by value (removes the first occurrence).
del deletes an item by index or can delete slices or entire variables/lists.
"""
# Diffn b/w append() & extend()
"""
append() adds its argument as a single element at the end of the list.
extend() adds each element of its argument (an iterable) individually to the end of the list.
"""
# Diffn b/w deep copy vs shallow copy
"""shallow copy shares nested objects, deep copy duplicates everything recursively"""

# List functions/methods
lst = [1, 2, 3, 4]
# methods
lst.append(5)       # [1, 2, 3, 4, 5]
lst.extend([6, 7])  # [1, 2, 3, 4, 5, 6, 7]
lst.insert(1, 0)    # [1, 0, 2, 3, 4, 5, 6, 7]
lst.pop()           # removes last: 7
lst.remove(2)       # removes first 2
lst.clear()         # empty list
lst.index(1)        # position of 3
lst.count(1)        # count of 1s
lst.sort()          # sort in place
lst.reverse()       # reverse in place
lst.copy()          # shallow copy
# build-in functions
len(lst)            # length
min(lst)            # minimum
max(lst)            # maximum
sum(lst)            # sum of numbers
sorted(lst)         # new sorted list
reversed(lst)       # iterator (list(reversed(lst)))

squares = [x**2 for x in lst]  # list comprehension
lst[1:4] # slicing