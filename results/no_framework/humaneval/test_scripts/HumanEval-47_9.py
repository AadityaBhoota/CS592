def median(l: list):
    """Return median of elements in the list l."""
    l_sorted = sorted(l)
    n = len(l_sorted)
    
    if n % 2 == 0:
        mid1 = n // 2 - 1
        mid2 = n // 2
        return (l_sorted[mid1] + l_sorted[mid2]) / 2
    else:
        mid = n // 2
        return l_sorted[mid]

# Test cases
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0



METADATA = {}


def check(candidate):
    assert candidate([3, 1, 2, 4, 5]) == 3
    assert candidate([-10, 4, 6, 1000, 10, 20]) == 8.0
    assert candidate([5]) == 5
    assert candidate([6, 5]) == 5.5
    assert candidate([8, 1, 3, 9, 9, 2, 7]) == 7 


check(median)