#pseudo-code
def bubble_sort(items: [int]):
    for scan in range(len(items) - 1):
        swapped = False
        for i in range(len(items) - 1 - scan):
            if items[i] > items[i+1]:
                swapped = True
                #items[i], items[i+1] = items[i+1], items[i]
                temp = items[i]
                items[i] = items[i+1]
                items[i+1] = temp

            if not swapped:
                break
        print(f"steps: {steps}")

# test
alist = [5,1,2,3,4]
bubble_sort(alist)
print(alist)

import random

def bubble_sort(items: [int]):
    steps = 0
    for scan in range(len(items) - 1):
        for i in range(len(items) - 1 - scan):
            steps += 1
            if items[i] > items[i+1]:
                #items[i], items[i+1] = items[i+1], items[i]
                temp = items[i]
                items[i] = items[i+1]


alist = random.sample(range(1,500),200)
alist_copy = alist[:] # create a copy of alist
bubble_sort(alist)
bubble_sort_improved(alist_copy)
print(alist)