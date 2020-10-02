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

def reverse_string(s: str):
    res = ""
    for i in range(len(s) -1, -1, -1):
        res += s[i]
    return res
print(reverse_string("work"))