# What are collections in Python?
"""
In Python, collections refers to the built-in data types and the collections module, 
which provides specialized, optimized container data types.

The collections module provides advanced data structures that make code cleaner, faster, and more readable.

| Type          | Use case                                  |
| ------------- | ----------------------------------------- |
| `defaultdict` | Auto-initialize missing keys              |
| `Counter`     | Count occurrences                         |
| `OrderedDict` | Maintain insertion order (pre-Python 3.7) |
| `namedtuple`  | Tuple with named fields                   |
| `deque`       | Fast append/pop from both ends            |

"""

# Interview Question
# Group transactions by user_id and calculate total amount spent by each user using collections.
transactions = [
    {"user_id": 1, "amount": 100},
    {"user_id": 2, "amount": 200},
    {"user_id": 1, "amount": 50},
]

from collections import defaultdict

result = defaultdict(int)

for txn in transactions:
    result[txn["user_id"]] += txn["amount"]

print(dict(result))
