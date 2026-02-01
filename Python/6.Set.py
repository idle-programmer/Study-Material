myset = {"apple", "banana", "cherry"}

# cannot access items in a set by referring to an index or a key.
# check using "in" keyword
# cannot change its items in set, but can add new items.
myset.add("orange")

# Add 2 set
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)

#The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
mylist = ["kiwi", "orange"]
thisset.update(mylist)

# remove element using remove() or discard() method, discard will not raise error if item not exist
# pop() method will remove item randomly
# clear() method will empty the set
# del keyword will delete the set


# How is data stored in a set? 
"""
Set: Hash-based storage

How it's stored internally:
A set uses a hash table. Each element's hash value decides where it is stored.
Elements are not stored in order.

Key characteristics:
❌ Unordered
❌ No duplicates
❌ No indexing
✅ Very fast lookup (O(1) average)
"""