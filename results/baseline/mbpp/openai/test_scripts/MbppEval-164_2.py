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
    div_sum = 0
    for i in range(1, n+1):
        if n % i == 0:
            div_sum += i
    return div_sum

def areEquivalent(num1, num2):
    return divisor_sum(num1) == divisor_sum(num2)

# Test cases




def check(candidate):
    assert are_equivalent(36, 57) == False
    assert are_equivalent(2, 4) == False
    assert are_equivalent(23, 47) == True

check(div_sum)