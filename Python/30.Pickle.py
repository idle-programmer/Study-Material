# What is Pickling and Unpickling?
"""
Pickling is the process of converting a Python object into a byte stream so it can be stored or transmitted.
Unpickling is the process of converting that byte stream back into the original Python object.

Why is it used?
Save Python objects to a file
Send objects over a network
Cache objects (e.g., Redis, disk cache)
Store model objects or intermediate results
"""

import pickle

data = {"name": "Mehul", "age": 26}

# Pickling (serialize)
with open("data.pkl", "wb") as f:
    pickle.dump(data, f)

# Unpickling (deserialize)
with open("data.pkl", "rb") as f:
    loaded_data = pickle.load(f)
