def check_min_heap_helper(arr, i):
    n = len(arr)
    
    # Check if the given index i has a left child and right child
    left = 2*i + 1
    right = 2*i + 2
    
    # Base case: If the index exceeds the size of the array, return True
    if i >= n:
        return True
    
    # Check if left child exists and is less than the parent
    if left < n and arr[left] < arr[i]:
        return False
    
    # Check if right child exists and is less than the parent
    if right < n and arr[right] < arr[i]:
        return False
    
    # Recursively check the left and right subtree
    return check_min_heap_helper(arr, left) and check_min_heap_helper(arr, right)

# Test cases




def check(candidate):
    assert check_min_heap([1, 2, 3, 4, 5, 6]) == True
    assert check_min_heap([2, 3, 4, 5, 10, 15]) == True
    assert check_min_heap([2, 10, 4, 5, 3, 15]) == False

check(check_min_heap_helper)