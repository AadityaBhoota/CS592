def median(l: list):
    """Return median of elements in the list l."""
    sorted_list = sorted(l)
    n = len(sorted_list)
    mid = n // 2  # Find the middle index
    if n % 2 == 0:  # If the list length is even
        return (sorted_list[mid - 1] + sorted_list[mid]) / 2
    else:  # If the list length is odd
        return sorted_list[mid]

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