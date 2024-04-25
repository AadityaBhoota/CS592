import math

def digits(n):
    """Given an integer n, return the product of the odd digits.
    Return 0 if all digits are even or n is negative.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    if n < 0:
        return 0

    product = 1
    for digit in str(abs(n)):
        if int(digit) % 2 != 0:
            product = math.prod([product, int(digit)])

    return product if product != 1 else 0

def check(candidate):

    # Check some simple cases
    assert candidate(5) == 5
    assert candidate(54) == 5
    assert candidate(120) ==1
    assert candidate(5014) == 5
    assert candidate(98765) == 315
    assert candidate(5576543) == 2625

    # Check some edge cases that are easy to work out by hand.
    assert candidate(2468) == 0


check(digits)