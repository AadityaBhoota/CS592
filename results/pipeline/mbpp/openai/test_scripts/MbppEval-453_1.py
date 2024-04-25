import math

def sumofFactors(n):
    sum_even_factors = 0

    for i in range(1, n+1):
        if n % i == 0 and i % 2 == 0:
            sum_even_factors += i
        if n % i == 0 and n // i != i and (n // i) % 2 == 0:
            sum_even_factors += n // i

    return sum_even_factors

def check(candidate):
    assert sumofFactors(18) == 26
    assert sumofFactors(30) == 48
    assert sumofFactors(6) == 8

check(sumofFactors)