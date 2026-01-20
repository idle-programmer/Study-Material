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

l=[i.lower() for i in l1]
d={}
for i in l:
    d[i]=d.get(i,0)+1
d1=sorted(d.items(),key=lambda x:x[1],reverse=True)
for i in d1:
    print(i[0])

# Find the largest and smallest number in a list without using built-in functions
l=[3,5,7,2,8,1,4]
largest=l[0]
smallest=l[0]
for i in l:
    if i>largest:
        largest=i
    if i<smallest:
        smallest=i
print("Largest:",largest)
print("Smallest:",smallest)

# Find the second largest number in a list
l=[3,5,7,2,8,1,4]
first=second=float('-inf')
for i in l:
    if i>first:
        second=first
        first=i
    elif first>i>second:
        second=i
print("Second Largest:",second)

# Find the missing number in a list of n-1 numbers ranging from 1 to n
l=[1,2,4,5,6]
n=len(l)+1
total_sum=n*(n+1)//2
actual_sum=sum(l)
missing_number=total_sum-actual_sum
print("Missing Number:",missing_number)

# Find all pairs in a list that sum up to a specific target
l=[1,2,3,4,5,6,7,8,9]
target=10
seen=set()
pairs=set()
for i in l:
    c=target-i
    if c in seen:
        pairs.add((min(i,c),max(i,c)))
    seen.add(i)
for pair in pairs:
    print(pair)

#add digits until a single digit remains
num = 38
if num==0:
    num=0
else:
    num=(1+(num-1)%9) # digital root formula
print(num)

# Palindrome Number
def isPalindrome(x: int) -> bool:
        if str(x)==str(x)[::-1]:
            return True
        return False

# Move all zeros to the end of the list
def shiftZero(l):
    p=0
    for i in range(len(l)):
        if l[i]!=0:
            l[p]=l[i]
            p+=1
        
    while p<len(l):
        l[p]=0
        p+=1
    return l 
print(shiftZero([1,0,2,0,3]))

# reverse list
def reverseList(lst):
    if not lst:
        return []
    return [lst[-1]] + reverseList(lst[:-1])

print(reverseList([1,2,3,4,5]))

# Check Correct String
def correctStr(str1):
    p=0
    for i in str1:
        if i =='(':
            p+=1
        elif i==')':
            p-=1
    return True if p==0 else False
str1='(hello(world)(one)two)'
print(correctStr(str1))