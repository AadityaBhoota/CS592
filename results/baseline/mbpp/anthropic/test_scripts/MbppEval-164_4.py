import math 
def div_sum(n): 
    '''
    Write a function to determine if the sum of the divisors of two integers are the same.

    Examples:
    areEquivalent(36,57) == False
    areEquivalent(2,4) == False
    areEquivalent(23,47) == True
    '''
import math

def divisor_sum(n):
    """
    Calculates the sum of all the divisors of a given number.
    """
    divisors_sum = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:
                divisors_sum += n // i
    return divisors_sum

def are_equivalent(a, b):
    """
    Determines if the sum of the divisors of two integers are the same.
    """
    return divisor_sum(a) == divisor_sum(b)

def check(candidate):
    assert are_equivalent(36, 57) == False
    assert are_equivalent(2, 4) == False
    assert are_equivalent(23, 47) == True

check(div_sum)