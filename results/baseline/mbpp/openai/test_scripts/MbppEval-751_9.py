def check_min_heap_helper(arr, i):
    n = len(arr)

    # If a leaf node is reached, return True
    if i >= n // 2:
        return True

    left_child = 2*i + 1
    right_child = 2*i + 2

    # Check if the current node is greater than its children
    if (left_child < n and arr[i] > arr[left_child]) or (right_child < n and arr[i] > arr[right_child]):
        return False

    # Recursively check the left and right subtrees
    return check_min_heap_helper(arr, left_child) and check_min_heap_helper(arr, right_child)

# Test the function with provided examples




def check(candidate):
    assert check_min_heap([1, 2, 3, 4, 5, 6]) == True
    assert check_min_heap([2, 3, 4, 5, 10, 15]) == True
    assert check_min_heap([2, 10, 4, 5, 3, 15]) == False

check(check_min_heap_helper)