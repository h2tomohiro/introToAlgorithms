"""
 String, List - Level 2.0
"""
import re

def count_hi(string):
    """
    Return the number of times that the string "hi" appears anywhere in the given string.
    """
    return string.count("hi")


def cat_dog(string):
    """
    Return True if the string "cat" and "dog" appear the same number of times in the given string.
    """
    cat = string.count("cat")
    dog = string.count("dog")
    if cat == dog:
        return True
    else:
        return False

def count_code(string):
    """
    Return the number of times that the string "code" appears anywhere in the given string,
    except it'll accept any letter for the 'd', so 'cope' and 'cooe' count.
    """
    a = re.findall("co[a-z]e", string)
    return len(a)

def end_other(a, b):
    """
    Given two strings, return True if either of the strings appears at the very end of the other string,
    ignoring upper/lower case differences (in other words, the computation should not be "case sensitive").
    Note: s.lower() returns the lowercase version of a string.
    """
    a = a.lower()
    b = b.lower()
    if len(a) >= len(b):
        l = len(b)
        if a[-l:] == b:
            return True
        else:
            return False
    if len(b) >= len(a):
        l = len(a)
        if b[-l:] == a:
            return True
        else:
            return False

def count_evens(nums):
    """
    Return the number of even ints in the given list.
    Note: the % 'mod' operator computes the remainder, e.g. 5 % 2 is 1.
    """
    l = []
    for i in nums:
        if i % 2 == 0:
            l.append(i)
    return len(l)


def big_diff(nums):
    """
    Given a list length 1 or more of ints, return the difference between the largest and smallest values in the array.
    Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.
    """
    return max(nums) - min(nums)

def sum13(nums):
    """
    Return the sum of the numbers in the list, returning 0 for an empty array.
    Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.
    """
    # a = [i for i, x in enumerate(nums) if x == 13]
    # l = a[]
    # s = 0
    # i = 0で13がデてきたタイミング＋1で要素が取れる
    # for i in a:
    #     l.append(a[i+1])
    # for i in nums:
    #     if i == 13:
    #         continue
    #     if i == nums:
    #         continue
    #     sum(nums)

def sum67(nums):
    """
    Return the sum of the numbers in the list, except ignore sections of numbers starting with a 6
    and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.
    """
    #6がデてきたら、次の7がデてくるまでずっと、処理を中止する
    # l = []
    # s = 0
    # for i in nums:
    #     if nums[i] == 6:
    #         while i != 7:
    #             continue
    #     else:
    #         l.append(i)

def has22(nums):
    """
    Given a list of ints, return True if the array contains a 2 next to a 2 somewhere.
    """
    # s = 0
    # for i in nums:
    #     if (nums[i] == 2):
    #         if (nums[i+1] == 2):
    #             return True
    #     else:
    #         return False