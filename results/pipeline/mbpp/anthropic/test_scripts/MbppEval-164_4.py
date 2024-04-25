import math

def div_sum(n):
    '''
    Write a function to determine the sum of the divisors of an integer.

    Example:
    div_sum(36) == 91
    div_sum(57) == 150
    '''
    divisors = []
    for i in range(1, n+1):
        if n % i == 0:
            divisors.append(i)
    return sum(divisors)

def areEquivalent(a, b):
    '''
    Write a function to determine if the sum of the divisors of two integers are the same.

    Examples:
    areEquivalent(36,57) == False
    areEquivalent(2,4) == False
    areEquivalent(23,47) == True
    '''
    return div_sum(a) == div_sum(b)

def check(candidate):
    assert are_equivalent(36, 57) == False
    assert are_equivalent(2, 4) == False
    assert are_equivalent(23, 47) == True

check(div_sum)