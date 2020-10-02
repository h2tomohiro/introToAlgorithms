""" Sorting Practice Problems """
# Write a program that sorts the first half of a list in ascending order
# and the second half in descending order.
# e.g. alist = [8, 1, 7, 5, 2, 4, 2, 9, 3, 6] the alist should be.
# changed to [1, 2, 5, 7, 8, 9, 6, 4, 3, 2]. This should work for other lists of course.

def sort_half(alist):
        for scan in range(len(alist) - 1):
            first_half = (len(alist) - 1) // 2
            min_index = scan
            for i in range(scan + 1, first_half + 1):
                if alist[i] < alist[min_index]:
                    min_index = i

            if min_index != scan:
                temp = alist[scan]
                alist[scan] = alist[min_index]
                alist[min_index] = temp

            second_half = (len(alist) // 2)
            for i in range(second_half, len(alist)):
                if alist[i] < alist[second_half]:
                    second_half = i

                if second_half != i:
                    temp = alist[second_half]
                    alist[second_half] = alist[i]
                    alist[i] = temp
        return alist

# 各配列をソートして並べる
# last_halfの並びを反転
# 最後に配列を連結する
def sort_half(alist):
    first_half = alist[:len(alist)//2]
    last_half = alist[len(alist)//2:]
    selection_sort(first_half)
    selection_sort(last_half)
    return first_half + last_half[::-1]

def selection_sort(alist):
    #steps = 0
    for scan in range(len(alist) - 1):
        min_index = scan
        for j in range(scan + 1, len(alist)):
            #steps += 1
            if alist[min_index] > alist[j]:
                min_index = j
        # swap
        if min_index != scan:
            alist[scan], alist[min_index] = alist[min_index], alist[scan]
alist = [8, 1, 7, 5, 2, 4, 2, 9, 3, 6]
print(sort_half(alist))

# Suppose two lists A and B have already been sorted.
# Elements of A have been sorted into ascending order and
# B has also been sorted in ascending order. Write a Python
# program to merge the elements of A and B into a list.
# At the end of the program the result list will contain
# all the elements of A and B in ascending order.

# def merge_two(A, B):
#     A.extend(B)
#     return sorted(A)

def merge_two(A, B):
    i = 0
    j = 0
    merged = []
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            merged.append(A[i])
            i += 1
        else:
            merged.append(B[j])
            j += 1
    if i == len(A):
        return merged + B[j:]
    else:
        return merged + A[i:]

# A = [1,2,3,4]
# B = [5,6,7,8]
# print(merge_two(A, B))

# Write a program to replace all negative values in a list
# called mylist with zeros. So, if mylist = [2, 5, -1, 3, 7, -2, 8],
# then mylist should be changed to [2, 5, 0, 3, 7, 0, 8]. This
# should of course work for other lists.

def replace_negative(mylist):
    for i in range(len(mylist)):
        if mylist[i] < 0:
            mylist[i] = 0
    return mylist
mylist = [2, 5, -1, 3, 7, -2, 8]
#print(replace_negative(mylist))