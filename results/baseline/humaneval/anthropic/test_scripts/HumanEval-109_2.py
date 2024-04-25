def move_one_ball(arr):
    """
    Determines if it is possible to get an array sorted in non-decreasing order
    by performing right shift operation any number of times.
    """
    if not arr:
        return True

    n = len(arr)
    for i in range(n):
        if all(arr[(i + j) % n] <= arr[(i + j + 1) % n] for j in range(n - 1)):
            return True
    return False

def check(candidate):

    # Check some simple cases
    assert candidate([3, 4, 5, 1, 2])==True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate([3, 5, 10, 1, 2])==True
    assert candidate([4, 3, 1, 2])==False
    # Check some edge cases that are easy to work out by hand.
    assert candidate([3, 5, 4, 1, 2])==False, "This prints if this assert fails 2 (also good for debugging!)"
    assert candidate([])==True

check(move_one_ball)