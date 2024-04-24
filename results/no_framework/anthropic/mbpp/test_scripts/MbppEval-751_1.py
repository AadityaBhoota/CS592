def check_min_heap_helper(arr, i):
    """
    Checks if the given array represents a min heap or not.

    Args:
        arr (list): The array to be checked.
        i (int): The index of the current node being checked.

    Returns:
        bool: True if the array represents a min heap, False otherwise.
    """
    n = len(arr)
    left_child_index = 2 * i + 1
    right_child_index = 2 * i + 2

    # Check if the current node is smaller than its children
    if left_child_index < n and arr[left_child_index] < arr[i]:
        return False
    if right_child_index < n and arr[right_child_index] < arr[i]:
        return False

    # Recursively check the left and right subtrees
    if left_child_index < n and not check_min_heap_helper(arr, left_child_index):
        return False
    if right_child_index < n and not check_min_heap_helper(arr, right_child_index):
        return False

    # If all checks pass, the current node and its subtrees form a min heap
    return True

def check(candidate):
    assert check_min_heap([1, 2, 3, 4, 5, 6]) == True
    assert check_min_heap([2, 3, 4, 5, 10, 15]) == True
    assert check_min_heap([2, 10, 4, 5, 3, 15]) == False

check(check_min_heap_helper)