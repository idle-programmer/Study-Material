# Store Data in key value pairs
# Ordered*, changable and do not allow duplicates
# accessed by key name
# get()
# keys() - list of keys
# values() - list of values
# items() - list of tupple of key:value pairs
# len()
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict.items())
# in keyword to check if key exists
# update() - update value of specific key or add key:value pair
# pop() or del keyword - remove item with specific key or entire dictionary
# clear() - empties dictionary
# dict() to make new or copy dictionary

# fromkeys() - make new dictionary from list of keys with same value
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
thisdict = dict.fromkeys(x) # default value is None
# setdefault() - returns value of specific key, if key does not exist insert key with specified value