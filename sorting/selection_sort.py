# l = [7, 4, 5, 2, 1, 9, 10, 3]
# index_min = 0
# for i in range(len(l)):
#     if l[i] < l[index_min]:
#         index_min = i
# print(index_min)
import random

def selection_sort(items: [int]):
    for scan in range(len(items) - 1):
        min_index = scan
        for i in range(scan + 1, len(items)):
            if items[i] < items[min_index]:
                min_index = i

        if min_index != scan: #if False, swapping the same value
            temp = items[scan]
            items[scan] = items[min_index]
            items[min_index] = temp

alist = random.sample(range(1, 500), 300)
selection_sort(alist)
print(alist)