# target = 34
# l = [1,3,4,5,7,10,12,21,34,35]
#
# def binary_search(items: [int], target: int) -> int:
#     """
#     Return the index of the target in the items if the target exists.
#     Otherwise, returns -1 if the target not found.
#     Using binary search algorithm
#     Time Complexity 0(lg N)
#     :param items:
#     :param target:
#     :return:
#     """
#     for i in range(len(items)):
#         if (items[] + items[])/2 >= target:
#            return 1
#         if (items[] + items[])/2 =< target:
#         　　return i
#     for i in range(len(items)):

def binary_search(alist, target):
    lower = 0
    upper = len(alist) - 1
    steps = 0

    while lower <= upper:
        mid = (lower + upper) // 2
        steps += 1
        if alist[mid] == target:
            return mid
        elif target < alist[mid]:
            lower = mid - 1
        else:
            upper = mid + 1

    #return -1, steps
    return -1, steps

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binary_search(testlist, 13))

#print(binary_search(testlist, 3))

# if __name__ == '__main__':
#     testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
#     print(binary_search(testlist, 3))
#     print(binary_search(testlist, 13))

    # countries = ["Australia", "Brazil", "Canada", "Denmark", "Ecuador",
    #              "France", "Germany", "Honduras", "Italy", "Japan",
    #              "Korea", "Letvia", "Malaysia", "Norway", "Oman", "Poland",
    #              "Qatar", "Russia", "Spain", "Thailand"
    #              ]
    # # lg 26 -> 4.xxx
    # target = "Italy"
    # pos, steps = binary_search(countries, target)
    # print(f"Found {target} at {pos} index in {steps} steps")

#recursive way
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

# testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
# print(binary_search(testlist, 1))
# print(binary_search(testlist, 17))

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