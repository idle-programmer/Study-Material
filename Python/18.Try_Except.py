"An exception is an error that occurs during program execution and breaks the normal flow."
"""
Code inside try runs If error occurs → jumps to except If no error → skips except.
else runs Only if no exception occurs.
finally always executes, whether exception occurs or not.
"""
try:
    x = int("10")
except ValueError:
    print("Conversion failed")
else:
    print("Conversion successful:", x)


try:
    file = open("data.txt")
    data = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    file.close()
    print("File closed")

"""Real-Life Use of finally 
Closing DB connections 
Closing files Releasing locks 
Cleaning resources"""


def withdraw(amount):
    if amount <= 0:
        raise ValueError("Amount must be positive")
    print("Withdrawn:", amount)

"""Why raise exceptions? 
To validate input 
To stop incorrect execution 
To enforce business rules"""

# Interview Question

# Difference b/w finally and else in try-except
"""else runs only if try succeeds (no exception).
finally runs always (cleanup code).

try → success → else → finally
try → exception → except → finally  
"""
