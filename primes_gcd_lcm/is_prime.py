import math
import time

def is_prime(n: int) -> bool:
    """ Check wether n is prime or not O(n)"""
    if n == 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

def is_prime(n: int) -> bool:
    """ Check whether n is prime or not O(n)"""
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % 1 == 0:
            return False
    return True

def generate_prime_list(n: int):
    prime_list = []
    for i in range(2, n + 1):
        if is_prime(i):
            prime_list.append(i)

    return prime_list

start_time = time.time()
generate_prime_list(10000000)
end_time = time.time()
print(f"{end_time - start_time} seconds")