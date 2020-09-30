""" group exercises 2 """
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
    if num > 1:
        print_binary(num // 2)
    if num < 0:
        num = int(str(num).lstrip('-'))
        print('-', end='')
        print_binary(num // 2)
    print(num % 2, end='')
#print_binary(4)

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


# *This is the answer teacher gave us.*
def eval_helper(expr: str, i: int) -> (int, int):
    if expr[i].isdigit():  # base case
        return int(expr[i]), i
    else:  # recursive case
        i += 1  # skip '('
        left, i = eval_helper(expr, i)
        i += 1  # skip left operand
        op = expr[i]
        i += 1
        right, i = eval_helper(expr, i)
        i += 1  # skip ')'
        if op == '*':
            return left * right, i
        else:
            return left + right, i

def evaluate(expr: str) -> int:
    i = 0
    return eval_helper(expr, i)[0]

# print(evaluate("7"))
# print(evaluate("(2+2)"))
# print(evaluate("(1+(2*4))"))
# print(evaluate("((1+3)+(5*(1+2)))"))


# Write a recursive function that accepts an integer number of digits
# and prints all base-10 numbers that have exactly that many digits, in
# ascending order, one per line.
#
# print_decimal(1)  prints from 0 to 9  (single digit)
# print_decimal(2)  prints from 10 to 99 (two digits)
# print_decimal(3)  prints from 100 to 999 (three digits)

def recur(n):
    if n <= 0:
        return 1
    return 10 * recur(n-1)

def print_decimal(digits):
    f = recur(digits - 1)
    e = recur(digits) - 1
    if digits == 1:
        for i in range(0, e + 1):
            print(i)
    elif digits > 1:
        for i in range(f, e + 1):
            print(i)
print_decimal(2)
