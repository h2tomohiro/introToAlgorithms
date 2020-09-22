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

def binarySearch(alist, target):
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

    return -1, steps

# testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
# print(binarySearch(testlist, 3))
# print(binarySearch(testlist, 13))

countries = ["Australia", "Brazil", "Canada", "Denmark", "Ecuador",
             "France", "Germany", "Honduras", "Italy", "Japan",
             "Korea", "Letvia", "Malaysia", "Norway", "Oman", "Poland",
             "Qatar", "Russia", "Spain", "Thailand"
             ]
# lg 26 -> 4.xxx
# target = "Italy"
# pos, steps = binary_search(countries, target)
# print(f"Found" {target} at {pos} index in {steps} steps)