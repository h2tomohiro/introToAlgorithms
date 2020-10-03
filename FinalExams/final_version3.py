""" Final Exam V3 """

# please submit your python file upon completion.

def is_anagram(s: str, t: str):
    """
    An anagram is a word or phrase formed by rearranging the
    letters of a different word or phrase, typically using all
    the letters exactly once.

    Given two strings s and t, write a program to
    determine if t is an anagram of s.
    You may assume that the string contains only lowercase alphabets.

    e.g.
    is_anagram("anagram", "nagaram") -> True
    is_anagram("rat", "car") -> False
    is_anagram("listen", "silent") -> True
    is_anagram("", "") -> True
    is_anagram("h", "e") -> False

    :param s: string
    :param t: string
    :return: True if s is an anagram of t, otherwise False
    """
    sort_s = ''.join(sorted(s))
    sort_t = ''.join(sorted(t))
    if sort_s == sort_t:
        return True
    else:
        return False

# s = "meo"
# t = "ome"
# print(is_anagram(s,t))

def remove_vowels(s: str):
    """
    Write an algorithm to remove all vowels from a string without replace() built-in method.
    You can write iteratively or recursively.

    e.g.
    remove_vowels("hello") -> "hll"
    remove_vowels("world") -> "wrld"
    remove_vowels("what") -> "wht"
    remove_vowels("") -> ""
    remove_vowels("a") -> ""

    :param s: string
    :return: string removed vowels
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    new_string = []
    for i in s:
        new_string.append(i)
        for j in vowels:
            if i == j:
                new_string.remove(j)
    return ''.join(new_string)

#print(remove_vowels('meo'))
