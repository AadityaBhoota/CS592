def check_min_heap_helper(arr, i):
    n = len(arr)

    left = 2 * i + 1
    right = 2 * i + 2

    # If the node is a leaf node
    if left >= n:
        return True

    # Check if the current node is greater than its children
    if (left < n and arr[i] > arr[left]) or (right < n and arr[i] > arr[right]):
        return False

    # Recursively check the left and right sub-trees
    return check_min_heap_helper(arr, left) and check_min_heap_helper(arr, right)

# Test cases




def check(candidate):
    assert check_min_heap([1, 2, 3, 4, 5, 6]) == True
    assert check_min_heap([2, 3, 4, 5, 10, 15]) == True
    assert check_min_heap([2, 10, 4, 5, 3, 15]) == False

check(check_min_heap_helper)