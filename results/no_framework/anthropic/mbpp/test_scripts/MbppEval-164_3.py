import math

def div_sum(n):
    """
    Write a function to determine if the sum of the divisors of two integers are the same.

    Examples:
    areEquivalent(36,57) == False
    areEquivalent(2,4) == False
    areEquivalent(23,47) == True
    """
    def sum_of_divisors(num):
        """Calculates the sum of divisors for a given number"""
        divisors_sum = 0
        for i in range(1, num + 1):
            if num % i == 0:
                divisors_sum += i
        return divisors_sum

    def areEquivalent(a, b):
        """Checks if the sum of divisors for two numbers are the same"""
        return sum_of_divisors(a) == sum_of_divisors(b)

    return areEquivalent

def check(candidate):
    assert are_equivalent(36, 57) == False
    assert are_equivalent(2, 4) == False
    assert are_equivalent(23, 47) == True

check(div_sum)