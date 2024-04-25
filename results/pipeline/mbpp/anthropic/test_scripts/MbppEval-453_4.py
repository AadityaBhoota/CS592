def sumofFactors(n):
    """
    Write a python function to find the sum of even factors of a number.

    Examples:
    sumofFactors(18) == 26
    sumofFactors(30) == 48
    sumofFactors(6) == 8
    """
    sum_of_even_factors = 0
    for i in range(1, n+1):
        if n % i == 0 and i % 2 == 0:
            sum_of_even_factors += i
    return sum_of_even_factors

def check(candidate):
    assert sumofFactors(18) == 26
    assert sumofFactors(30) == 48
    assert sumofFactors(6) == 8

check(sumofFactors)