def intersection(interval1, interval2):
    start1, end1 = interval1
    start2, end2 = interval2

    # Determine the intersection
    start = max(start1, start2)
    end = min(end1, end2)

    if start > end:
        return "NO"  # No intersection

    # Calculate the length of the intersection
    length = end - start + 1

    # Determine the output based on the length of the intersection
    if length == 1:
        return "NO"
    elif is_prime(length):
        return "YES"
    else:
        return "NO"

def is_prime(n):
    """
    Helper function to check if a number is prime.
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

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