import math

def sumofFactors(n):
    """
    Write a python function to find the sum of even factors of a number.

    Examples:
    sumofFactors(18) == 26
    sumofFactors(30) == 48
    sumofFactors(6) == 8
    """
    sum = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if i % 2 == 0:
                sum += i
            if (n // i) % 2 == 0 and (n // i) != i:
                sum += n // i
    if int(math.sqrt(n)) ** 2 == n:
        sum += int(math.sqrt(n))
    return sum

def check(candidate):
    assert sumofFactors(18) == 26
    assert sumofFactors(30) == 48
    assert sumofFactors(6) == 8

check(sumofFactors)