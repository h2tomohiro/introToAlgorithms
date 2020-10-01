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
    next = []
    for i in range(0,len(pre)):
        for j in range(0,len(word)):
            nextString = pre[i][0:j]+word[0]+pre[i][j:len(word)-1]
            if nextString not in next:
                next.append(nextString)
    return(next)
print(permutation("tomo"))


from typing import List
DiceResult = List[List[int]]

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
    results = []
    dice_sum_helper(dice, desired_sum, [], results)
    return results

def dice_sum_helper(dice: int, desired_sum: int, chosen: List[int], results: DiceResult):
    if dice == 0 and sum(chosen) == desired_sum:
        results.append(chosen.copy())
    elif dice == 0:
        return
    else:
        for i in range(1, 7):
            chosen.append(i)
            dice_sum_helper(dice - 1, desired_sum, chosen, results)
            chosen.pop()
print(sum_of_dice(3,6))