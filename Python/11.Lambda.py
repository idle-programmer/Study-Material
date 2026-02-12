"""
Docstring for Python.11.Lambda

A lambda function in Python is an anonymous (nameless) function defined using the lambda keyword,
allowing a single expression to be evaluated and returned.
It has the syntax lambda arguments: expression and is useful for short, one-off functions 
without needing a full def definition.

A lambda function can take any number of arguments, but can only have one expression.
"""
square = lambda x: x * x
print(square(5))  # Output: 25

users = [('John', 28, 'Engineer'), ('Alice', 25, 'Designer'), ('Bob', 30, 'Manager')]
# Sort by age, then by name
sorted_users = sorted(users, key=lambda x: (x[1], x[0]))
print(sorted_users)



# Count frequency of each fruit in the list and print them in descending order of frequency
l1=["Pear", "Banana", "Grapes", "Apples", "Pear", "apples", "Oranges", "Oranges", "Pear", "Pear"]
l2= [item.lower() for item in l1]
d1={}
for item in l2:
    d1[item]=d1.get(item,0)+1

fl= sorted(d1.items() ,key=lambda x:-x[1])
for i, j in fl:
    print(i)