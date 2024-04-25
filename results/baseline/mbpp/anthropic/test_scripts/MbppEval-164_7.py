import math

def div_sum(n):
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

def areEquivalent(a, b):
    """
    Determines if the sum of the divisors of two integers are the same.
    """
    return div_sum(a) == div_sum(b)

# Examples




def check(candidate):
    assert are_equivalent(36, 57) == False
    assert are_equivalent(2, 4) == False
    assert are_equivalent(23, 47) == True

check(div_sum)