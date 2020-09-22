from searching.linear_search import *
from searching.binary_search import *

# def linear_search(items: [str], target: str) -> str:
#     for i in range(len(items)):
#         if items[i] == target:
#             return i
#     return -1
#
# def binary_search(alist, target):
#     lower = 0
#     upper = len(alist) - 1
#     steps = 0
#
#     while lower <= upper:
#         mid = (lower + upper) // 2
#         steps += 1
#         if alist[mid] == target:
#             return mid
#         elif target < alist[mid]:
#             lower = mid - 1
#         else:
#             upper = mid + 1
#
#     return -1, steps
#
with open("words") as f:
    lines = f.readlines()

converted_list = []
for line in lines:
    converted_list.append(line.strip().lower())

target = input("Search word:").lower()
li = linear_search(converted_list, target)
bi = binary_search(converted_list, target)

print(f"Linear Search: found at {0}, took {0} steps")
print(f"Binary Search: found at {0}, took {0} steps")