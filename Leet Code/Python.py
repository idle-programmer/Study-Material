# 1 Write a python program to add two numbers without using + operator
a=2
b=3
while b!=0:
    c=a&b
    a=a^b
    b=c<<1
print(a)

# Count frequency of each fruit in the list and print them in descending order of frequency
l1=["Pear", "Banana", "Grapes", "Apples", "Pear", "apples", "Oranges", "Oranges", "Pear", "Pear"]