def move_one_ball(arr):
    if not arr:  # Step 0: Check if the input array is empty
        return True
    
    # Step 1: Find the index of the minimum element in the array
    min_index = arr.index(min(arr))
    
    # Step 2: Calculate the number of right shifts needed to bring the minimum element to the first position
    num_shifts = len(arr) - min_index
    
    # Step 4: Create a new array by performing the right shifts
    new_arr = arr[-min_index:] + arr[:-min_index]
    
    # Step 5: Check if the new array is sorted in non-decreasing order
    is_sorted = all(new_arr[i] <= new_arr[i+1] for i in range(len(new_arr)-1))
    
    return is_sorted

def check(candidate):

    # Check some simple cases
    assert candidate([3, 4, 5, 1, 2])==True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate([3, 5, 10, 1, 2])==True
    assert candidate([4, 3, 1, 2])==False
    # Check some edge cases that are easy to work out by hand.
    assert candidate([3, 5, 4, 1, 2])==False, "This prints if this assert fails 2 (also good for debugging!)"
    assert candidate([])==True

check(move_one_ball)