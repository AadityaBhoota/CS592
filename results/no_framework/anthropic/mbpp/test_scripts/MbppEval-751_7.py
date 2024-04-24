def check_min_heap_helper(arr, i):
    """
    Recursively checks if the given array represents a min heap.

    Args:
        arr (list): The array to be checked.
        i (int): The index of the current node being checked.

    Returns:
        bool: True if the array represents a min heap, False otherwise.
    """
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    # Base case: If the current node is a leaf, it is considered a min heap.
    if left_child >= len(arr) and right_child >= len(arr):
        return True

    # Check if the current node satisfies the min heap property.
    if left_child < len(arr) and arr[i] > arr[left_child]:
        return False
    if right_child < len(arr) and arr[i] > arr[right_child]:
        return False

    # Recursively check the left and right subtrees.
    return check_min_heap_helper(arr, left_child) and check_min_heap_helper(arr, right_child)

def check(candidate):
    assert check_min_heap([1, 2, 3, 4, 5, 6]) == True
    assert check_min_heap([2, 3, 4, 5, 10, 15]) == True
    assert check_min_heap([2, 10, 4, 5, 3, 15]) == False

check(check_min_heap_helper)