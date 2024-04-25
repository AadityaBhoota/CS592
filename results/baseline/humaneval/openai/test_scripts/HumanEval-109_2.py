def move_one_ball(arr):
    if not arr:
        return True

    n = len(arr)
    min_index = arr.index(min(arr))
    
    # Checking if the array is already sorted
    if all(arr[i] <= arr[i+1] for i in range(n-1)):
        return True

    for i in range(n):
        if arr[min_index] == arr[(min_index+1)%n]:
            return True
        min_index = (min_index+1) % n

    return False

# Test cases



def check(candidate):

    # Check some simple cases
    assert candidate([3, 4, 5, 1, 2])==True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate([3, 5, 10, 1, 2])==True
    assert candidate([4, 3, 1, 2])==False
    # Check some edge cases that are easy to work out by hand.
    assert candidate([3, 5, 4, 1, 2])==False, "This prints if this assert fails 2 (also good for debugging!)"
    assert candidate([])==True

check(move_one_ball)