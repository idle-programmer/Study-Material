# Quick sort

# Not in-place Quick Sort
l=[3,4,1,4,5,1,4,1,3,5,2]
import random
def QS1(l):
    if len(l)<=1:
        return l
    pivot = random.choice(l)
    left = [x for x in l if x<pivot]
    middle = [x for x in l if x==pivot]
    right = [x for x in l if x>pivot]
    return QS1(left)+middle+QS1(right)

# print(QS1(l))

# In-place Quick Sort
def QS2(l,start,end):
    if start>=end:
        return
    pivot=l[end] # last ele as pivot
    boundary = start # boundary for smaller elements
    for i in range(start,end):
        if l[i]<pivot:
            l[i],l[boundary]=l[boundary],l[i]
            boundary+=1

    l[boundary],l[end]=l[end],l[boundary] # place pivot in correct position
    QS2(l,start,boundary-1)
    QS2(l,boundary+1,end)

# QS2(l,0,len(l)-1)
# print(l)

