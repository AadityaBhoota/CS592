import math

def div_sum(n):
    """
    Write a function to determine if the sum of the divisors of two integers are the same.

    Examples:
    areEquivalent(36,57) == False
    areEquivalent(2,4) == False
    areEquivalent(23,47) == True
    """
    def sum_divisors(x):
        divisors = set()
        for i in range(1, int(math.sqrt(x)) + 1):
            if x % i == 0:
                divisors.add(i)
                divisors.add(x // i)
        return sum(divisors)

    def areEquivalent(a, b):
        return sum_divisors(a) == sum_divisors(b)

    return areEquivalent

def check(candidate):
    assert are_equivalent(36, 57) == False
    assert are_equivalent(2, 4) == False
    assert are_equivalent(23, 47) == True

check(div_sum)