def is_prime(n):
    """
    Helper function to check if a number is prime.
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def intersection(interval1, interval2):
    """
    Determines whether the length of intersection of two intervals is a prime number.
    """
    start1, end1 = interval1
    start2, end2 = interval2

    # Check if the intervals intersect
    if start1 > end2 or start2 > end1:
        return "NO"

    # Compute the intersection
    intersect_start = max(start1, start2)
    intersect_end = min(end1, end2)
    intersect_length = intersect_end - intersect_start + 1

    # Check if the length of the intersection is prime
    if is_prime(intersect_length):
        return "YES"
    else:
        return "NO"

def check(candidate):

    # Check some simple cases
    assert candidate((1, 2), (2, 3)) == "NO"
    assert candidate((-1, 1), (0, 4)) == "NO"
    assert candidate((-3, -1), (-5, 5)) == "YES"
    assert candidate((-2, 2), (-4, 0)) == "YES"

    # Check some edge cases that are easy to work out by hand.
    assert candidate((-11, 2), (-1, -1)) == "NO"
    assert candidate((1, 2), (3, 5)) == "NO"
    assert candidate((1, 2), (1, 2)) == "NO"
    assert candidate((-2, -2), (-3, -2)) == "NO"


check(intersection)