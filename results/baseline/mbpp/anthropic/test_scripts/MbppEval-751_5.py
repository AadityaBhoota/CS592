def check_min_heap_helper(arr, i):
    """
    Checks if the given array represents a min heap or not.

    Args:
        arr (list): The array to be checked.
        i (int): The index of the current node.

    Returns:
        bool: True if the array represents a min heap, False otherwise.
    """
    left_child_index = 2 * i + 1
    right_child_index = 2 * i + 2

    # Check if the current node is greater than its left or right child
    if left_child_index < len(arr) and arr[i] > arr[left_child_index]:
        return False
    if right_child_index < len(arr) and arr[i] > arr[right_child_index]:
        return False

    # Recursively check the left and right subtrees
    if left_child_index < len(arr) and not check_min_heap_helper(arr, left_child_index):
        return False
    if right_child_index < len(arr) and not check_min_heap_helper(arr, right_child_index):
        return False

    # If all checks pass, the array represents a min heap
    return True

def check_min_heap(arr):
    """
    Checks if the given array represents a min heap.

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