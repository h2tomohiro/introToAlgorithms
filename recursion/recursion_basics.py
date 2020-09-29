# iterative way (loop)
def print_stars(n: int):
    for i in range(n):
        print("*", end="")

#print_stars(3)

# recursive way(without loops)
def print_stars_recur(n: int):
    # base case(trivial case)
    # assume that n >= 1
    if n == 1:
        print("*", end="")
    # recursive case
    # (you do a little bit of work yourself,
    # and call the same function for the rest of the work
    else:
        print("*", end="")
        print_stars_recur(n - 1)

#print_stars_recur(10)

# factorial (iteratively)
def factoarial(n: int) -> int:
    res = 1
    for i in range(2, n + 1):
        res *= i # res = res * i
    return res


# factorial (recursively)
def factorial_recur(n: int) -> int:
    # base case
    if n == 0:
        return 1
    return n * factorial_recur(n - 1)

# power (iteratively) Faster way
def power(base, exp):
    res = 1
    for _ in range(exp):
        res *= base
    return res

# power(recursively)
def power_recur(base, exp):
    # base case
    if exp == 0:
        return 1
    # recursive case
    return base * power(base, exp - 1)

# 1,1,2,3,5,8,13,21,...
def fibonacci(n):
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    return b
#print(fibonacci(0))

# 1,1,2,3,5,8,13,21,...
# slow
def fibonacci_recur(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci_recur(n - 1) + fibonacci_recur(n - 2)
#print(fibonacci_recur(4))

# LeetCode
# Too slow
def tribonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)
#print(tribonacci(25))

def tribonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)
#print(tribonacci(25))

def tribonacci_improved(n):
    # if n == 0:
    #     return 0
    # elif n == 1 or n == 2:
    #     return 1
    # else:
    #     return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)
    # t0 = 0
    # t1 = 1
    # t2 = 1
    # for i in range(3, n - 2):
    #     t1, t2 = t0 + t1 + t2, t0 + t1 + t2
    # return t2
    if n == 0:
        return 0
    t0 = 0
    t1 = 1
    t2 = 1
    for i in range(3, n + 1):
        t0, t1, t2 = t1, + t2, t0 + t1 + t2
    return t2
print(tribonacci(4))