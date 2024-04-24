def move_one_ball(arr):
    """
    Determines if it is possible to get an array sorted in non-decreasing order
    by performing right shift operation any number of times.
    """
    if not arr:
        return True
    
    # Check if the array is already sorted
    if all(arr[i] <= arr[i+1] for i in range(len(arr)-1)):
        return True
    
    # Perform right shift operation and check if the array is now sorted
    for i in range(len(arr)):
        shifted_arr = arr[1:] + [arr[0]]
        if all(shifted_arr[i] <= shifted_arr[i+1] for i in range(len(shifted_arr)-1)):
            return True
        arr = shifted_arr
    
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