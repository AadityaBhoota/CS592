import math 
def div_sum(n): 
    '''
    Write a function to determine if the sum of the divisors of two integers are the same.

    Examples:
    areEquivalent(36,57) == False
    areEquivalent(2,4) == False
    areEquivalent(23,47) == True
    '''
def divisor_sum(n):
    """
    Calculates the sum of all the divisors of an integer n.
    """
    divisor_sum = 0
    for i in range(1, n+1):
        if n % i == 0:
            divisor_sum += i
    return divisor_sum

def are_divisor_sums_equal(a, b):
    """
    Determines if the sum of the divisors of two integers are the same.
    """
    return divisor_sum(a) == divisor_sum(b)

def check(candidate):
    assert are_equivalent(36, 57) == False
    assert are_equivalent(2, 4) == False
    assert are_equivalent(23, 47) == True

check(div_sum)