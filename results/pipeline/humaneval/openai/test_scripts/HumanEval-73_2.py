def smallest_change(arr):
    # Step 1: Identify indices where elements need to be changed
    n = len(arr)
    change_indices = [i for i in range(n // 2) if arr[i] != arr[n - i - 1]]
    
    # Step 2: Initialize variable count to 0
    count = 0
    
    # Step 3: Iterate through the change_indices list
    for index in change_indices:
        # Step 4: Find the minimum change required at the current index
        count += min(abs(arr[index] - arr[n - index - 1]), 26 - abs(arr[index] - arr[n - index - 1]))
        
    return count

def check(candidate):

    # Check some simple cases
    assert candidate([1,2,3,5,4,7,9,6]) == 4
    assert candidate([1, 2, 3, 4, 3, 2, 2]) == 1
    assert candidate([1, 4, 2]) == 1
    assert candidate([1, 4, 4, 2]) == 1

    # Check some edge cases that are easy to work out by hand.
    assert candidate([1, 2, 3, 2, 1]) == 0
    assert candidate([3, 1, 1, 3]) == 0
    assert candidate([1]) == 0
    assert candidate([0, 1]) == 1


check(smallest_change)