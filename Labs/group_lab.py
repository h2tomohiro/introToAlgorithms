""" group exercises 2 """
import re

# Write a recursive function printBinary that accepts integer and
# prints that number's representation in binary (base 2)
#
# Examples:
# print_binary(2)    prints 10
# print_binary(7)    prints 111
# print_binary(12)   prints 1100
# print_binary(42)   prints 101010
# print_binary(-500) prints -111110100
def print_binary(num):
    if num >= 1:
        print_binary(num // 2)
        print(num % 2, end='')
    elif num < 0:
        num = int(str(num).lstrip('-'))
        print('-', end='')
        print_binary(num // 2)
        print(num % 2, end='')

print_binary(2)


# Write a recursive function evaluate that accepts a string
# representing a math expression and computes its value.
# - The expression will be "fully parenthesized" and will
#   consist of + and * on single-digit integers only.
# - You can use a helper function. (Do not change the original function header)
# - Recursion
#
# evaluate("7")                 -> 7
# evaluate("(2+2)"              -> 4
# evaluate("(1+(2*4))"          -> 9
# evaluate("((1+3)+((1+2)*5))") -> 19

# 括弧の中身を取り出す
# 中身を計算する
# 表示させる
# def evaluate(expr):

#evaluate(1)


# Write a recursive function that accepts an integer number of digits
# and prints all base-10 numbers that have exactly that many digits, in
# ascending order, one per line.
#
# print_decimal(1)  prints from 0 to 9  (single digit)
# print_decimal(2)  prints from 10 to 99 (two digits)
# print_decimal(3)  prints from 100 to 999 (three digits)
def print_decimal(digits):
    if digits == 0:
        print("none")
    elif digits == 1:
        n = 10 ** (digits - 1)
        print(0-9)
    elif digits > 1:
        n = 10 ** (digits - 1)
        return print_decimal(digits)
        #return print_decimal(n+1)
#print_decimal(1)
    # if len(n_str) == digits:
    #     print(n,end="")
    #     n = 10**(digits-1) + 1
    #     print_decimal(n)
    # elif len(n_str) > digits:
    #     return False
    # n = str(n)
    # return len(n)
    #
    # if n == 0:
    #     return 0
    # return 1 + print_decimal(10**(digits-1))



