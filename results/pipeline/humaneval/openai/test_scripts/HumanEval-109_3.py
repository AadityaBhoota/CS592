def move_one_ball(arr):
    if not arr:
        return True

    min_index = arr.index(min(arr))

    # Check if the array is already sorted
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            break
    else:
        return True
    
    num_shifts = len(arr) - min_index
    if num_shifts == len(arr):
        num_shifts = 0

    new_arr = arr[-min_index:] + arr[:-min_index]

    for i in range(len(new_arr) - 1):
        if new_arr[i] > new_arr[i + 1]:
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