import math

def sumofFactors(n):
    """
    Write a python function to find the sum of even factors of a number.

    Examples:
    sumofFactors(18) == 26
    sumofFactors(30) == 48
    sumofFactors(6) == 8
    """
    total = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if i % 2 == 0:
                total += i
            if n // i != i and (n // i) % 2 == 0:
                total += n // i
    return total

def check(candidate):
    assert sumofFactors(18) == 26
    assert sumofFactors(30) == 48
    assert sumofFactors(6) == 8

check(sumofFactors)