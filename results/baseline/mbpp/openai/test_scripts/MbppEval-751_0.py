def check_min_heap_helper(arr, i):
    # Get the indices of left and right children of node i
    left = 2*i + 1
    right = 2*i + 2

    # Check if left child is within array bounds and is smaller than the parent
    if left < len(arr) and arr[left] < arr[i]:
        return False

    # Check if right child is within array bounds and is smaller than the parent
    if right < len(arr) and arr[right] < arr[i]:
        return False

    # Recursively check left and right subtrees
    if left < len(arr) and not check_min_heap_helper(arr, left):
        return False

    if right < len(arr) and not check_min_heap_helper(arr, right):
        return False

    return True

# Test cases




def check(candidate):
    assert check_min_heap([1, 2, 3, 4, 5, 6]) == True
    assert check_min_heap([2, 3, 4, 5, 10, 15]) == True
    assert check_min_heap([2, 10, 4, 5, 3, 15]) == False

check(check_min_heap_helper)