example = "Hello, World!"

# ----Slicing---- #
print(example[2:5])  # starting and ending index, end position will be x-1

print(example[:5])  # non starting value will start from 0

print(example[2:])  # non ending value will traval till end of string

print(example[-5:-2])  # "-" negative indexing works for reverse slicing


# ----Modify Strings---- #
print(example.upper())

print(example.lower())

# removes space from start and end of string, also has lstrip and rstrip
print(example.strip())

# replace the given char of string,
print(example.replace("H", "B"))

# Replace the two first occurrence of the word if number given
print(example.replace("l", "B", 2))

print(example.split(","))  # created a list of text between the given seperator,

# if number given after seperator it will only split to the given number
print(example.split(",", 0))


# ----String Concatenation---- #
a = "Hello"
b = "World"
c = a + b


# ----F-Strings---- #
age = 36
txt = f"My name is John, I am {age}"
txt = f"My name is John, I am {age*10}"
txt = f"My name is John, I am {age:.2f}"  # modifier is included by adding a colon ":"


