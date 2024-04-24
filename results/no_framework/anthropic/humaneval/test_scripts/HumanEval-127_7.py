def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def intersection(interval1, interval2):
    """
    Determines whether the length of intersection of two intervals is a prime number.
    
    Args:
        interval1 (tuple): The first interval, represented as a tuple of (start, end).
        interval2 (tuple): The second interval, represented as a tuple of (start, end).
    
    Returns:
        str: "YES" if the length of the intersection is a prime number, "NO" otherwise.
    """
    start1, end1 = interval1
    start2, end2 = interval2
    
    # Check if the intervals intersect
    if start1 > end2 or start2 > end1:
        return "NO"
    
    # Calculate the intersection
    intersection_start = max(start1, start2)
    intersection_end = min(end1, end2)
    intersection_length = intersection_end - intersection_start + 1
    
    # Check if the length of the intersection is a prime number
    if is_prime(intersection_length):
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