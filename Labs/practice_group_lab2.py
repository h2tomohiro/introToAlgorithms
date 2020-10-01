def permutation(word: str):
    """
    Write a recursive function permutation that accepts a string as a parameter
    and outputs all possible rearrangements of the letters in the string.
    The arrangements may be output in any order.
    example)
    permutation("park")
    output: park, pakr, pkar, prak, arpk, aprk, akrp, ...
    :param word: word to permute
    :return: display permutations of a given word
    """
    if len(word) == 0:
        return ['']
    pre = permutation(word[1:len(word)])
    print(pre)
    next = []
    for i in range(0,len(pre)):
        for j in range(0,len(word)):
            nextString = pre[i][0:j]+word[0]+pre[i][j:len(word)-1]
            if nextString not in next:
                next.append(nextString)
    return next
#print(permutation("tomo"))

def sum_of_dice(dice: int, desired_sum: int):
    """
    Prints all possible outcomes of rolling the given number of six-sided dice
    that add up to the given desired sum, in {#, #, #} format.

    :param dice: the number of dice
    :param desired_sum: desired sum
    :return: display all possible ways
    example)
    sum_of_dice(2, 7)
    output: {1, 6}, {2, 5}, {3, 4}, {4, 3}, {5, 2}, {6, 1}
    """
    # if the number of dice > desired_sum
    # return False or something
    # elif the number of dice >= desired_sum
    # a + b = int


    #sum_of_dice(1, 6) {6}
    #sum_of_dice(3, 4) {1,1,2},{1,2,1},{2,1,1}
    # サイコロの数
    # サイコロの数で実現できるパターンを表示
    # def print_binary(num: int):
    #     print(print_binary_helper(num))
    #
    # def print_binary_helper(num: int) -> str:
    #     if num < 0:
    #         return "-" + print_binary_helper(num * -1)
    #     if num == 0:
    #         return ""
    #     if num % 2 == 0:
    #         return print_binary_helper(num // 2) + "0"
    #     else:
    #         return print_binary_helper(num // 2) + "1"


# import itertools
# origin_list = ['1','2','3','4','5','6']
# dice = int
# desired_sum = int
#
# for i, _ in enumerate(origin_list, 1):
#     for j in itertools.permutations(origin_list, r=i):  # rには1、2、3と渡される
#         print(j)

# import itertools
#
# def create_gen(string):
#     for char in string:
#         yield char
#
# # list()でリストにする
# origin_list = list(create_gen('12'))
# for i, _ in enumerate(origin_list, 1):
#     for j in itertools.permutations(origin_list, r=i):  # rには1、2、3と渡される
#         print(j)

# import itertools
#
# dice = [1,2,3,4,5,6]
# l = []
#
# def subsets(n,m):
#     perms = itertools.combinations(dice, n)
#     for i in perms:
#      if sum(i) == m:
#       l.append(i)
#     return l
# print(subsets(2,7))
# def sum_of_dice(n,m):
#     for i in itertools.permutations(subsets(n,m)):
#         print(i)


#print(subsets(2,7))


# for i in itertools.permutations(l):
#     print(i)

# list()でリストにする
# origin_list = list(create_gen('))
# for i, _ in enumerate(origin_list, 1):
#     for j in itertools.permutations(origin_list, r=i):  # rには1、2、3と渡される
#         print(j)

from typing import List
DiceResult = List[List[int]]

def dice_sum(num_dice: int, target_sum: int):
    results = []
    dice_sum_helper(num_dice, target_sum, [], results)
    return results

def dice_sum_helper(num_dice: int, target_sum: int, chosen: List[int], results: DiceResult):
    if num_dice == 0 and sum(chosen) == target_sum:
        results.append(chosen.copy())
    elif num_dice == 0:
        return
    else:
        for i in range(1, 7):
            chosen.append(i)
            dice_sum_helper(num_dice - 1, target_sum, chosen, results)
            chosen.pop()
print(dice_sum(2,6))