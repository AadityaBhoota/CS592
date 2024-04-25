def move_one_ball(arr):
    """Determine if it is possible to get an array sorted in non-decreasing order
    by performing right shift operation any number of times.

    Args:
        arr (list): The input array of integers.

    Returns:
        bool: True if it is possible to sort the array, False otherwise.
    """
    if not arr:
        return True

    # Sort the array to get the target sorted order
    target = sorted(arr)

    # Check if the array is already sorted
    if arr == target:
        return True

    # Iterate through the array and check if a right shift can be performed
    for i in range(len(arr)):
        if arr[i] == target[0]:
            # Perform the right shift operation
            arr = arr[i:] + arr[:i]
            # Check if the array is now sorted
            if arr == target:
                return True

    # If no right shift operation can be performed, return False
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