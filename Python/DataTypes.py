"""Numeric Types : Integer, Float, Complex Numbers"""

int
x = 8  # immutable
float
y = 1.8  # immutable
complex
z = 1j

"""Sequence Types : List, Tuple, Range, String (also text type)"""
list
a = [1, 2, 3, 4]
tuple
b = (1, 2, 3, 4)  # immutable
range
c = range(4)
str
d = "my string"

"""Mapping Types : Dictionary"""
dict
e = {"key": "value"}

"""Set Types : Set, frozenset"""
set
f = {"a", "b", "c"}
frozenset
g = frozenset({"a", "b", "c"})

"""Boolean Type : Bool"""
h = True / False

"""Binary Type : bytes"""
i = b"jkl"

"""None Type : bytes"""
m = None


#Interview Questions
#1. Differentiate between list, tuple, set, dictionary and Array?
""" A list is an ordered, mutable collection that can contain duplicate and mixed data types. 
Lists are indexed by integers and declared with square brackets, like. You can change, add, or remove items freely.​

A tuple is similar to a list but is immutable, meaning you cannot change its values once defined. 
Tuples are also indexed and can contain mixed types and duplicates, declared with parentheses (1, 2, 3).​

Sets are unordered, mutable collections with unique elements only. Unlike lists and tuples, sets do not support indexing 
and are declared with curly braces {1, 2, 3}. They are useful for removing duplicates or performing set operations.​

A dictionary is a mutable and unordered collection. It stores data as key-value pairs, where keys are unique 
and values can be of any type. Dictionaries are declared with curly braces using the key:value syntax, such as {1: "a", 2: "b"}.​

Arrays are ordered, mutable, and typically hold elements of a single data type. Unlike lists, arrays require importing the array module
and are more memory-efficient if you need many numeric values. Arrays are declared with the array() function, e.g., array('i', )."""

"""
A list in Python can store elements of different types, is built-in, and can grow or shrink dynamically. 
An array, on the other hand, stores only elements of the same data type, is more memory-efficient, 
requires importing the array module, and is optimized for numerical operations.​
Lists are best for general-purpose data storage with high flexibility, 
while arrays are preferred for handling large amounts of numeric data where performance and memory efficiency are important.
"""
#2. What are built-in data types in Python?
""" Built-in data types in Python include:
1. Numeric Types: int, float, complex
2. Sequence Types: list, tuple, range, string
3. Mapping Type: dictionary
4. Set Types: set, frozenset
5. Boolean Type: bool
6. Binary Types: bytes, bytearray, memoryview
7. None Type: NoneType
These data types allow you to store and manipulate different kinds of data in Python. """

#3. what is mutable in python?
""" In Python, mutable objects are those that can be changed or modified after they are created. 
Examples of mutable data types include lists, dictionaries, and sets."""

#4.What is range and xrange in Python?
""" In Python 2, range() returns a list of numbers, while xrange() returns an xrange object that generates numbers on demand (more memory efficient). 
In Python 3, xrange() is removed, and range() behaves like xrange() from Python 2, returning a range object that generates numbers on demand. """