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

def get_divisors(n):
    divisors = []
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.remove(n)
    return divisors

def areEquivalent(num1, num2):
    sum_divisors_num1 = sum(get_divisors(num1))
    sum_divisors_num2 = sum(get_divisors(num2))
    return sum_divisors_num1 == sum_divisors_num2

# Test cases




def check(candidate):
    assert are_equivalent(36, 57) == False
    assert are_equivalent(2, 4) == False
    assert are_equivalent(23, 47) == True

check(div_sum)