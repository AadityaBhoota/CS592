import math

def sumofFactors(n):
    even_factors = []
    for i in range(1, n+1):
        if n % i == 0 and i % 2 == 0:
            even_factors.append(i)
    return sum(even_factors)

def check(candidate):
    assert sumofFactors(18) == 26
    assert sumofFactors(30) == 48
    assert sumofFactors(6) == 8

check(sumofFactors)