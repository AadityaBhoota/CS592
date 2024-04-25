from functools import reduce

def gcd(a, b):
    """
    Helper function to calculate the greatest common divisor of two numbers.
    """
    while b:
        a, b = b, a % b
    return a

def largest_subset(a):
    """
    Finds the size of the largest subset of a list of numbers where every pair is divisible.
    """
    if not a:
        return 0

    # Calculate the greatest common divisor of all the numbers in the list
    gcd_all = reduce(gcd, a)

    # Find the largest subset where every pair is divisible
    return sum(1 for num in a if num % gcd_all == 0)

def check(candidate):
    assert largest_subset([ 1, 3, 6, 13, 17, 18 ]) == 4
    assert largest_subset([10, 5, 3, 15, 20]) == 3
    assert largest_subset([18, 1, 3, 6, 13, 17]) == 4

check(largest_subset)