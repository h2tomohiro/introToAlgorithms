def count_even(start: int, end: int) -> int:
    """
    Returns the number of even numbers between start and end
    """
    #偶数を返す
    l = []
    for i in range(start, end+1):
        if i % 2 == 0:
            l.append(i)
        return l

    #奇数
        l = []
        for i in range(start, end+1):
            if i % 2 != 0:
                l.append(i)
        return l

    #奇数の合計
        l = []
        for i in range(start, end+1):
            if i % 2 != 0:
                l.append(i)
            i = sum(l)
        return i

    #偶数の合計
        l = []
        for i in range(start, end+1):
            if i % 2 == 0:
                l.append(i)
            i = sum(l)
        return i

def binary_search_recursive(arr, elem, start=0, end=None):
    if end is None:
        end = len(arr) - 1
    if start > end:
        return False
    mid = (start + end) // 2
    if elem == arr[mid]:
        return mid
    if elem < arr[mid]:
        return binary_search_recursive(arr, elem, start, mid - 1)
    # elem > arr[mid]
    return binary_search_recursive(arr, elem, mid + 1, end)

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binary_search_recursive(testlist, 32))

#Iterative solution:
def binary_search_iterative(arr, elem):
    start, end = 0, (len(arr) - 1)
    while start <= end:
        mid = (start + end) // 2
        if elem == arr[mid]:
            return mid
        if elem < arr[mid]:
            end = mid - 1
        else:  # elem > arr[mid]
            start = mid + 1
    return False

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binary_search_iterative(testlist, 32))

def reverse_string(s: str):
    res = ""
    for i in range(len(s) -1, -1, -1):
        res += s[i]
    return res
#print(reverse_string("work"))

## bubble Sort
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)

import sys

A = [64, 25, 12, 22, 11]

# Traverse through all array elements
for i in range(len(A)):

    # Find the minimum element in remaining
    # unsorted array
    min_idx = i
    for j in range(i + 1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j

            # Swap the found minimum element with
    # the first element
    A[i], A[min_idx] = A[min_idx], A[i]

#Driver code to test above
l = []
for i in range(len(A)):
    l.append(A[i])
print(l),

