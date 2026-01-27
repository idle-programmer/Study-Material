"""
An iterator is an object that contains a countable number of values and can be iterated upon, 
meaning you can traverse through all its values. Technically, in Python, an iterator is an object 
that implements the iterator protocol, which consists of the methods __iter__() and __next__().
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


# Generators
"""
A generator is a function that produces values one at a time instead of all at once.
It remembers where it stopped and continues from there.
uses yield instead of return.
low memory usage.
return ends function, yield pauses it.
"""

def get_attendance_records():
    for i in range(1, 1_000_000):
        yield f"Employee-{i}"

for record in get_attendance_records():
    print(record)

# Usecase of generator
"""
Reading large files.
Pagination
Django QuerySets"""

# Interview Question

"""
UseCases of Iterators
* When querying millions of rows from a database, loading all rows in memory is impossible. Backend teams use iterators to stream rows gradually.
* DevOps or backend systems must read huge log files where loading entire file is impossible, so iterators are used to read file in chunk. Avoids memory overflow.
* APIs (Django/FastAPI/Flask) often need to process items in batches.
"""

# Generators vs Iterators
"Generators is a type of iterators. it automatically implement __iter__() and __next__() methods."


"""
An iterable is any object that can be looped over, like a list or range. 
An iterator is an object that keeps track of iteration state and returns elements using next(). 
A generator is a special type of iterator created using the yield keyword that produces values lazily and is memory efficient. 
range is a built-in iterable that generates numbers on demand without storing them in memory.
"""

# Difference b/w normal function and generator function
"""| Aspect   | Normal Function                          | Generator Function                   |
| ----------- | ---------------------------------------- | ------------------------------------ |
| Keyword     | return                                   | yield                                |
| Execution   | Runs completely, returns one value, ends | Pauses at yield, resumes next time   |
| Return type | Single value / None                      | Generator object (iterator)          |
| Memory      | Creates all data first                   | Lazy - generates one value at a time |
| Reusable    | Yes                                      | No - exhausted after one iteration   |"""