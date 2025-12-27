# Interview Questions

# What is Memory Management in Python?
"""Memory management in Python involves the allocation, deallocation, 
and optimization of memory usage for objects created during program execution. 
Python uses an automatic memory management system that includes a private heap 
containing all Python objects and data structures."""

# How does Python manage memory?
"""Python manages memory using a combination of reference counting and  garbage collection.
Reference counting keeps track of how many references point to an object. When the count drops to zero, the object is deallocated.
Garbage collection handles circular references that reference counting alone cannot detect, ensuring all unreachable objects are eventually freed."""

# Types of Memory in Python
# Stack memory : stors local variables and function calls
def func():
    x = 10   # x reference is on stack
func()

# Heap memory : stores objects and data structures
a = [1, 2, 3] # list object is on heap

# Private Python memory manager : manages heap memory allocation

# Garbage Collection : reclaims memory from unreachable objects, especially in circular references

# Circular Reference Example
a = []
b = []
a.append(b)
b.append(a)

import gc
gc.collect()  # Manually trigger garbage collection

# Reference Counting : tracks number of references to each object for deallocation when count reaches zero
a = []
b = a
c = b

# Advanced Topics
"""Memory Pools & Arenas (Advanced but Useful)
Python doesn't ask OS for memory every time.
Instead:
    Arenas → big chunks
    Pools → medium
    Blocks → small

This makes Python faster.
Python uses memory pooling to reduce frequent system calls."""

"""
Immutable vs Mutable (Memory Behavior)
a = 10
a = a + 1 # New int object created, old one unchanged (immutable)

lst = [1,2]
lst.append(3) # Same list object modified (mutable)
"""

def demo():
    x = [1,2,3]
    return x

y = demo()
"""
| Step          | Memory                  |
| ------------- | ----------------------- |
| x created     | Stack reference         |
| list          | Heap                    |
| return        | x reference transferred |
| function ends | stack cleaned           |
| y exists      | heap object alive       |
"""