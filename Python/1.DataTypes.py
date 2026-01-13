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

my_range = range(1, 1000001)  # Creates a range object, not a list

# Iterate over some numbers – only the needed numbers are generated
for i in my_range:
    if i > 5:
        break
    print(i)

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
h = True and False

"""Binary Type : bytes"""
i = b"jkl"

"""None Type : bytes"""
m = None


#Interview Questions
#1. Differentiate between list, tuple, set, dictionary and Array?
""" A list is an ordered, mutable , contain duplicate & mixed datatypes. Indexed by integers.

Tuple =  immutable, meaning you cannot change its values once defined. 
Indexed & contain mixed types & duplicates, declared with parentheses (1, 2, 3).​

Sets = unordered, mutable collections with unique elements only. No indexing 
& declared with curly braces {1, 2, 3}. They are useful for removing duplicates or performing set operations.​

Dictionary =  mutable and unordered collection. Stores data as key-value pairs, where keys are unique 
and values can be of any type. Declared with curly braces using the key:value syntax, such as {1: "a", 2: "b"}.​

Arrays = ordered, mutable, and typically hold elements of a single data type. Require importing the array module
and are more memory-efficient if you need many numeric values. Declared with the array() function, e.g., array('i', )."""

"""
A list can store elements of mixed types, is built-in, and can grow or shrink dynamically. 
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

#Is python compiled lang or interpreted lang? Why?
"""Python is interpreted because there's no separate compilation step—you run source code directly.
Internally, it compiles to bytecode first (hidden from user), then the PVM interprets bytecode line-by-line. 
This gives immediate feedback but slower runtime vs fully compiled languages like C++."""

#What is .py & .pyc?
""".py = Source code (human-readable Python code you write).
.pyc = Compiled bytecode (machine-readable, faster to load).

| Aspect     | .py                        | .pyc                  |
| ---------- | -------------------------- | --------------------- |
| Content    | Source code                | Bytecode              |
| Readable   | Yes                        | No                    |
| Created by | You                        | Python automatically  |
| Speed      | Slower (compile each time) | Faster (pre-compiled) |
| Location   | Your project               | __pycache__/ folder   |

.pyc speeds up imports by skipping recompilation. 
Python checks .py timestamp—if changed, recompiles to new .pyc."""

# what is pythonpath?
"""PYTHONPATH is an environment variable that adds directories to sys.path. 
Python searches these paths for modules during import. Useful for custom project 
structures or local development.
"""
import sys
print(sys.path)  # Shows all search paths (PYTHONPATH included)
