def move_one_ball(arr):
    """
    Given an array of integers, determine if it is possible to get the array
    sorted in non-decreasing order by performing right shift operations.
    """
    if not arr:
        return True
    
    sorted_arr = sorted(arr)
    
    for _ in range(len(arr)):
        if arr == sorted_arr:
            return True
        arr = [arr[-1]] + arr[:-1]
    
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