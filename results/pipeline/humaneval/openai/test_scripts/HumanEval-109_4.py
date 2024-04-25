def move_one_ball(arr):
    # Step 0: Check if the array is already sorted
    if arr == sorted(arr):
        return True
    
    # Step 1: Find the index of the minimum element in the array
    min_index = arr.index(min(arr))
    
    # Step 2: Handle multiple occurrences of the minimum element
    next_min_index = arr[min_index+1:].index(min(arr)) + min_index + 1 if min(arr) in arr[min_index+1:] else min_index
    
    # Step 3: Check if elements to the left of the minimum element are sorted
    if arr[:min_index] == sorted(arr[:min_index]):
        
        # Step 4: Check if elements to the right of the minimum element are sorted
        if arr[min_index+1:] == sorted(arr[min_index+1:]):
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