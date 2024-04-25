def check_min_heap_helper(arr, i):
    left_child_idx = 2 * i + 1
    right_child_idx = 2 * i + 2
    
    # Check if the current node satisfies the min-heap property
    if left_child_idx < len(arr) and arr[left_child_idx] < arr[i]:
        return False
    if right_child_idx < len(arr) and arr[right_child_idx] < arr[i]:
        return False
    
    # Recursively check the left and right subtrees
    if left_child_idx < len(arr):
        if not check_min_heap_helper(arr, left_child_idx):
            return False
    if right_child_idx < len(arr):
        if not check_min_heap_helper(arr, right_child_idx):
            return False
    
    # If we reach this point, the min-heap property is satisfied
    return True

def check(candidate):
    assert check_min_heap([1, 2, 3, 4, 5, 6]) == True
    assert check_min_heap([2, 3, 4, 5, 10, 15]) == True
    assert check_min_heap([2, 10, 4, 5, 3, 15]) == False

check(check_min_heap_helper)