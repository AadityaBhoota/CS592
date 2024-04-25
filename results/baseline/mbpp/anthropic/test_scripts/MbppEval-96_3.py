def divisor(n):
    '''
    Write a python function to find the number of divisors of a given integer.

    Examples:
    divisor(15) == 4
    divisor(12) == 6
    divisor(9) == 3
    '''
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    return count

def check(candidate):
    assert divisor(15) == 4
    assert divisor(12) == 6
    assert divisor(9) == 3

check(divisor)