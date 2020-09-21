def without_end(string):
    """
    Given a string, return a version without the first and last char, so "Hello" yields "ell".
    The string length will be at least 2.
    """
    s = string[:-1]
    t = s[1:]
    return t

def non_start(a, b):
    """
    Given 2 strings, return their concatenation, except omit the first char of each.
    The strings will be at least length 1.
    """
    a = without_end(a)
    b = without_end(b)
    return a + b

non_start("Hello","nomowosss")