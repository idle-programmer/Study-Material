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


# Merge sort
def merge(left, right):
    result = []

    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    return result + left + right
    
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)
        
arr= [2,1,3,4,5,7,6]
print(merge_sort(arr))


def insertion_sort(arr):
    n=len(arr)
    
    for i in range(1,n):
        key = arr[i]
        j=i-1
        
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
            
        arr[j+1]=key
        
arr= [2,1,3,4,5,7,6]
# insertion_sort(arr)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            print(j+1)
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped: 
            break #Stops early if array is already sorted.
        
arr= [2,1,3,4,5,7,6]
# bubble_sort(arr)