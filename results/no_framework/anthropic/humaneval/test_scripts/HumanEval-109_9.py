def move_one_ball(arr):
    """
    Determine if it is possible to get an array sorted in non-decreasing order
    by performing the right shift operation any number of times.
    """
    if not arr:
        return True

    # Sort the input array
    sorted_arr = sorted(arr)

    # Check if the input array is already sorted
    if arr == sorted_arr:
        return True

    # Perform the right shift operation and check if the array becomes sorted
    for _ in range(len(arr)):
        arr = [arr[-1]] + arr[:-1]
        if arr == sorted_arr:
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