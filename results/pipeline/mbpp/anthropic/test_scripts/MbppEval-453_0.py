import math

def sumofFactors(n):
    factors = [i for i in range(1, n+1) if n % i == 0]
    even_factors = [f for f in factors if f % 2 == 0]
    return sum(even_factors)

def check(candidate):
    assert sumofFactors(18) == 26
    assert sumofFactors(30) == 48
    assert sumofFactors(6) == 8

check(sumofFactors)