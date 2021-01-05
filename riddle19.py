# -*- coding: utf-8 -*-

import math


def get_prime_factors(n):
    factors = set()
    # Add the number of two's that divide n
    while n % 2 == 0:
        factors.add(2)
        n = n / 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        # while i divides n, add i and divide n
        while n % i == 0:
            factors.add(i)
            n = n / i

    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        factors.add(n)

    return list(factors)


def list_prime_factors(z):
    factors = []
    n = 0
    y = 0
    while y < z:
        n += 1
        # First check if 7, 11 or 13 are prime factors of n to speed up
        if not (n % 7 == 0 or n % 11 == 0 or n % 13 == 0 or n == 1) or n == 0:
            continue

        # Check there is no more prime numbers than 7, 11 and 13
        factors = get_prime_factors(n)
        difference = [i for i in factors if i not in [7, 11, 13]]
        if len(difference) == 0 or n == 1:
            y += 1
            factors.append(y)
            print(f"{y} - {n}", end='\n', flush=True)
    return factors


prime_numbers = list_prime_factors(200)
print(prime_numbers[200])

# Solution (after ~10h running ...) : 1185367183
