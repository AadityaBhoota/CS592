import math 
def count_divisors(n) : 
    '''
    Write a python function to check whether the count of divisors is even. 
    Examples:
    count_Divisors(10) == "Even"
    count_Divisors(100) == "Odd"
    count_Divisors(125) == "Even"
    '''
import math

def is_even_divisors(n):
    """
    Check whether the count of divisors of a number n is even.
    """
    # Find the prime factorization of n
    prime_factors = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            prime_factors.append(i)
            n //= i
        else:
            i += 1
    if n > 2:
        prime_factors.append(n)

    # Calculate the number of divisors
    num_divisors = 1
    for factor in prime_factors:
        num_divisors *= (factor + 1)

    # Determine if the number of divisors is even or odd
    if num_divisors % 2 == 0:
        return "Even"
    else:
        return "Odd"

def check(candidate):
    assert count_divisors(10)
    assert not count_divisors(100)
    assert count_divisors(125)

check(count_divisors)