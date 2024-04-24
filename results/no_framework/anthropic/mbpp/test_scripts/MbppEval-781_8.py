import math

def count_divisors(n):
    """
    Write a python function to check whether the count of divisors is even.
    Examples:
    count_Divisors(10) == "Even"
    count_Divisors(100) == "Odd"
    count_Divisors(125) == "Even"
    """
    divisors = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors += 1
            if i != n // i:
                divisors += 1
    if divisors % 2 == 0:
        return "Even"
    else:
        return "Odd"

def check(candidate):
    assert count_divisors(10)
    assert not count_divisors(100)
    assert count_divisors(125)

check(count_divisors)