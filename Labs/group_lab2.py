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
    # if len(word) < 2:
    #     yield word
    #     return
    # for pos in range(0, len(word)):
    #     char = word[pos]
    #     Remaining = list(permutation(word[0:pos] + word[pos + 1:]))
    #     for perm in Remaining:
    #         yield char + perm
    if len(word) == 0:
        return ['']
    prevList = permutation(word[1:len(word)])
    nextList = []
    for i in range(0,len(prevList)):
        for j in range(0,len(word)):
            newString = prevList[i][0:j]+word[0]+prevList[i][j:len(word)-1]
            if newString not in nextList:
                #print(newString)
                nextList.append(newString)
    return nextList

    # 順列の数だけ存在する？
    # 文字の数だけ繰り返す？
print(permutation("mark"))

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
    #sum_of_dice(1, 6) {6}
    #sum_of_dice(3, 4) {1,1,2},{1,2,1},{2,1,1}
    # サイコロの数
    # サイコロの数で実現できるパターンを表示

    pass