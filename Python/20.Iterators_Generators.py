"""
An iterator is an object that contains a countable number of values.
An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().
"""

# Iterator vs Iterable
"""
Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.
All these objects have a iter() method which is used to get an iterator:
"""
tup = (1, 2, 3, 4, 5)  # tupple
itr1 = iter(tup)  # returns iterator object
print(next(itr1))

stri = "abcde"  # strings are iterable objects
itr2 = iter(stri)
print(next(itr2))

# Iterator is the reason by which we can use for/while loops to iterate
# The for loop actually creates an iterator object and executes the next() method for each loop.

# Interview Question

"""
UseCases of Iterators
* When querying millions of rows from a database, loading all rows in memory is impossible. Backend teams use iterators to stream rows gradually.
* DevOps or backend systems must read huge log files where loading entire file is impossible, so iterators are used to read file in chunk. Avoids memory overflow.
* APIs (Django/FastAPI/Flask) often need to process items in batches.
"""
