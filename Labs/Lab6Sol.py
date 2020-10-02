""" Primes, GCD, LCM """
import math

def is_prime(n):
    """ Check if n is prime """
    if n <= 1: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(15))

def gcd(a, b):
    """ GCD of a and b """
    # 最大公約数
    while b != 0:
        a, b = b, a % b

    return a
print(gcd(6,12))

def lcm(a, b):
    """ LCM of a and b """
    # 最大公倍数
    # aとbを掛けて、最大公約数で割ったもの
    return a * b // gcd(a, b)
#print(lcm(6,12))



def generate_primes(n):
    """
    Generating a list of primes
    :return: a list of primes from 2 to n
    """
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes
