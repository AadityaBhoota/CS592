import math

def div_sum(n):
    """
    Write a function to determine if the sum of the divisors of two integers are the same.

    Examples:
    areEquivalent(36,57) == False
    areEquivalent(2,4) == False
    areEquivalent(23,47) == True
    """
    def sum_of_divisors(x):
        total = 0
        for i in range(1, int(math.sqrt(x)) + 1):
            if x % i == 0:
                total += i
                if i != x // i:
                    total += x // i
        return total

    a, b = n
    return sum_of_divisors(a) == sum_of_divisors(b)

def check(candidate):
    assert are_equivalent(36, 57) == False
    assert are_equivalent(2, 4) == False
    assert are_equivalent(23, 47) == True

check(div_sum)