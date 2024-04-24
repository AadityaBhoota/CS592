def check_min_heap_helper(arr, i):
    """
    Check if the given array represents a min heap.
    
    Args:
        arr (list): The array to be checked.
        i (int): The index of the current node being checked.
    
    Returns:
        bool: True if the array represents a min heap, False otherwise.
    """
    n = len(arr)
    
    # Check if the current node satisfies the min-heap property
    left_child = 2 * i + 1
    right_child = 2 * i + 2
    
    if left_child < n and arr[left_child] < arr[i]:
        return False
    
    if right_child < n and arr[right_child] < arr[i]:
        return False
    
    # Recursively check the left and right subtrees
    if left_child < n and not check_min_heap_helper(arr, left_child):
        return False
    
    if right_child < n and not check_min_heap_helper(arr, right_child):
        return False
    
    return True

def check(candidate):
    assert check_min_heap([1, 2, 3, 4, 5, 6]) == True
    assert check_min_heap([2, 3, 4, 5, 10, 15]) == True
    assert check_min_heap([2, 10, 4, 5, 3, 15]) == False

check(check_min_heap_helper)