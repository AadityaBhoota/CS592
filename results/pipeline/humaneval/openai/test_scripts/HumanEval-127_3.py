def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def intersection(interval1, interval2):
    start1, end1 = min(interval1), max(interval1)
    start2, end2 = min(interval2), max(interval2)
    
    intersect_start = max(start1, start2)
    intersect_end = min(end1, end2)
    
    if intersect_start > intersect_end:
        return "NO"
    
    intersection_length = intersect_end - intersect_start
    
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