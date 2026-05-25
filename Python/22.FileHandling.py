# What is context manager?
"""A context manager is an object that manages resource setup and cleanup using the with statement. 
It implements __enter__() and __exit__(). The __enter__() method is called when entering the block 
and usually acquires the resource, while __exit__() is called when leaving the block and is responsible 
for cleanup such as closing files, database connections, or releasing locks. If an exception occurs 
inside the with block, Python passes the exception details to __exit__(), allowing it to handle cleanup 
and optionally suppress the exception by returning True.

example:

with open("data.txt", "r") as file:
    content = file.read()
"""