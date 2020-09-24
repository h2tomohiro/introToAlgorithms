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

alist = [8, 1, 7, 5, 2, 10, 11, 4, 2, 9, 3, 6, 8, 9, 10, 11]
sort_half(alist)
print(alist)


# Suppose two lists A and B have already been sorted.
# Elements of A have been sorted into ascending order and
# B has also been sorted in ascending order. Write a Python
# program to merge the elements of A and B into a list.
# At the end of the program the result list will contain
# all the elements of A and B in ascending order.


def merge_two(A, B):
    pass


# Write a program to replace all negative values in a list
# called mylist with zeros. So, if mylist = [2, 5, -1, 3, 7, -2, 8],
# then mylist should be changed to [2, 5, 0, 3, 7, 0, 8]. This
# should of course work for other lists.


def replace_negative(mylist):
    pass

