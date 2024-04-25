def is_prime(n):
    """Helper function to check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def intersection(interval1, interval2):
    """Determine if the length of the intersection of two intervals is a prime number."""
    # Determine the intersection of the two intervals
    start = max(interval1[0], interval2[0])
    end = min(interval1[1], interval2[1])
    
    # If the intervals don't intersect, return "NO"
    if start > end:
        return "NO"
    
    # Calculate the length of the intersection
    length = end - start + 1
    
    # Check if the length is a prime number
    if is_prime(length):
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