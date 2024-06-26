def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    # Sort the list in ascending order
    l.sort()
    
    # Get the length of the list
    n = len(l)
    
    # If the length of the list is odd, return the middle element
    if n % 2 != 0:
        return l[n // 2]
    # If the length of the list is even, return the average of the two middle elements
    else:
        mid1 = l[n // 2 - 1]
        mid2 = l[n // 2]
        return (mid1 + mid2) / 2



METADATA = {}


def check(candidate):
    assert candidate([3, 1, 2, 4, 5]) == 3
    assert candidate([-10, 4, 6, 1000, 10, 20]) == 8.0
    assert candidate([5]) == 5
    assert candidate([6, 5]) == 5.5
    assert candidate([8, 1, 3, 9, 9, 2, 7]) == 7 


check(median)