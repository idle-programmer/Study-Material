# what is memoization?
"""
Memoization is an optimization technique where function results are cached 
so repeated calls with the same inputs return the stored result instead of recomputing.
"""

# without memoization
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)


# WITH memoization (manual way)
memo = {}
def fib(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]


# Pythonic way (using lru_cache)
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

