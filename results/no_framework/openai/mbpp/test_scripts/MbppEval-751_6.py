def check_min_heap_helper(arr, i):
    n = len(arr)

    # If a leaf node is reached, it is a min heap
    if i >= n // 2:
        return True

    left = 2 * i + 1
    right = 2 * i + 2

    # Check if the current node is greater than its children
    if (left < n and arr[left] < arr[i]) or (right < n and arr[right] < arr[i]):
        return False

    # Recursively check the left and right subtrees
    return check_min_heap_helper(arr, left) and check_min_heap_helper(arr, right)

# Test cases




def check(candidate):
    assert check_min_heap([1, 2, 3, 4, 5, 6]) == True
    assert check_min_heap([2, 3, 4, 5, 10, 15]) == True
    assert check_min_heap([2, 10, 4, 5, 3, 15]) == False

check(check_min_heap_helper)