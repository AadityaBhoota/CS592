def check_min_heap_helper(arr, i):
    """
    Checks if the given array represents a min heap starting from the index `i`.
    
    Args:
    arr (list): The input array.
    i (int): The index from where the min heap property needs to be checked.
    
    Returns:
    bool: True if the array represents a min heap, False otherwise.
    """
    left_child_idx = 2 * i + 1
    right_child_idx = 2 * i + 2
    
    # Base case: If the current node is a leaf node, it satisfies the min heap property
    if left_child_idx >= len(arr) and right_child_idx >= len(arr):
        return True
    
    # Check if the current node satisfies the min heap property
    if left_child_idx < len(arr) and arr[i] > arr[left_child_idx]:
        return False
    if right_child_idx < len(arr) and arr[i] > arr[right_child_idx]:
        return False
    
    # Recursively check the left and right subtrees
    return check_min_heap_helper(arr, left_child_idx) and check_min_heap_helper(arr, right_child_idx)

def check(candidate):
    assert check_min_heap([1, 2, 3, 4, 5, 6]) == True
    assert check_min_heap([2, 3, 4, 5, 10, 15]) == True
    assert check_min_heap([2, 10, 4, 5, 3, 15]) == False

check(check_min_heap_helper)