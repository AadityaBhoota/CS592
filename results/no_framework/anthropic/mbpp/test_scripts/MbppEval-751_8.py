def check_min_heap_helper(arr, i):
    """
    Recursive function to check if the given array represents a min heap.
    
    Args:
    arr (list): The array to be checked.
    i (int): The index of the current node being checked.
    
    Returns:
    bool: True if the array represents a min heap, False otherwise.
    """
    left_child_index = 2 * i + 1
    right_child_index = 2 * i + 2
    
    # Base case: If the current node is a leaf node, return True
    if left_child_index >= len(arr) and right_child_index >= len(arr):
        return True
    
    # Check if the current node satisfies the min-heap property
    if left_child_index < len(arr) and arr[left_child_index] < arr[i]:
        return False
    if right_child_index < len(arr) and arr[right_child_index] < arr[i]:
        return False
    
    # Recursively check the left and right subtrees
    return check_min_heap_helper(arr, left_child_index) and check_min_heap_helper(arr, right_child_index)

def check_min_heap(arr):
    """
    Check if the given array represents a min heap.
    
    Args:
    arr (list): The array to be checked.
    
    Returns:
    bool: True if the array represents a min heap, False otherwise.
    """
    return check_min_heap_helper(arr, 0)

def check(candidate):
    assert check_min_heap([1, 2, 3, 4, 5, 6]) == True
    assert check_min_heap([2, 3, 4, 5, 10, 15]) == True
    assert check_min_heap([2, 10, 4, 5, 3, 15]) == False

check(check_min_heap_helper)