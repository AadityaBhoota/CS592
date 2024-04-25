def monotonic(l: list):
    """Return True if list elements are monotonically increasing or decreasing."""
    
    # Step 0: Check if the list is empty
    if not l:
        return True
    
    # Step 1.1: Check if the list is strictly sorted in increasing order
    is_increasing = all(l[i] < l[i+1] for i in range(len(l) - 1))
    
    # Step 1.2: Check if the list is strictly sorted in decreasing order
    is_decreasing = all(l[i] > l[i+1] for i in range(len(l) - 1))

    # Step 2: Return True if either strictly increasing or strictly decreasing
    return is_increasing or is_decreasing



METADATA = {}


def check(candidate):
    assert candidate([1, 2, 4, 10]) == True
    assert candidate([1, 2, 4, 20]) == True
    assert candidate([1, 20, 4, 10]) == False
    assert candidate([4, 1, 0, -10]) == True
    assert candidate([4, 1, 1, 0]) == True
    assert candidate([1, 2, 3, 2, 5, 60]) == False
    assert candidate([1, 2, 3, 4, 5, 60]) == True
    assert candidate([9, 9, 9, 9]) == True


check(monotonic)