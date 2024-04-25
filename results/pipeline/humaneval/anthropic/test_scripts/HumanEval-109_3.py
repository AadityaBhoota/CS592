def move_one_ball(arr):
    if not arr:
        return True

    # Find the index of the smallest element
    min_idx = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[min_idx]:
            min_idx = i

    # Check if the array can be rotated
    for i in range(len(arr)):
        if arr[(i + min_idx) % len(arr)] != arr[i]:
            return False

    return True

def check(candidate):

    # Check some simple cases
    assert candidate([3, 4, 5, 1, 2])==True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate([3, 5, 10, 1, 2])==True
    assert candidate([4, 3, 1, 2])==False
    # Check some edge cases that are easy to work out by hand.
    assert candidate([3, 5, 4, 1, 2])==False, "This prints if this assert fails 2 (also good for debugging!)"
    assert candidate([])==True

check(move_one_ball)