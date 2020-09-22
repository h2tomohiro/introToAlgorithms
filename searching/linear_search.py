import random
def linear_search(items: [int], target: int) -> int:
    """
    Return the index of the target in the items if the target exists.
    Otherwise, returns -1 if the target not found.
    :param items: a list of items
    :param target: the item we're searching for
    :return: the index of the target in the items if the target exists. Otherwise, returns -1 if the target not found.
    """
    for i in range(len(items)):
        if items[i] == target:
            return i
    return -1

if __name__ == '__main__':

    # Generate a list of random numbers(size of 100)
    search_items = random.sample(range(1,1000), 100)
    print(search_items)

    index = random.randint(0,99)
    print(search_items[index])
    print(f"target index: {index}")

    # Searching for 150 in search_items
    print(index == linear_search(search_items, search_items[index]))