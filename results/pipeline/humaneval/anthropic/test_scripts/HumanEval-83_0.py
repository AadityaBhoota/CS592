def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    total = 10 ** n
    starts_with_1 = 10 ** (n - 1)
    ends_with_1 = 10 ** (n - 1)
    both_1 = 1
    return starts_with_1 + ends_with_1 - both_1

def check(candidate):

    # Check some simple cases
    assert True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate(1) == 1
    assert candidate(2) == 18
    assert candidate(3) == 180
    assert candidate(4) == 1800
    assert candidate(5) == 18000

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"


check(starts_one_ends)