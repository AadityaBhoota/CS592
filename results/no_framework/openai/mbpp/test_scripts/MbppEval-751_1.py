def check_min_heap_helper(arr, i):
    # Base case: leaf nodes are valid min heap
    if i >= len(arr) // 2:
        return True
    
    left_child = 2 * i + 1
    right_child = 2 * i + 2
    
    # Check if current node is less than or equal to its children
    if (left_child < len(arr) and arr[i] <= arr[left_child]) and \
       (right_child < len(arr) and arr[i] <= arr[right_child]):
        return check_min_heap_helper(arr, left_child) and check_min_heap_helper(arr, right_child)
    else:
        return False

# Test the function with given examples




def check(candidate):
    assert check_min_heap([1, 2, 3, 4, 5, 6]) == True
    assert check_min_heap([2, 3, 4, 5, 10, 15]) == True
    assert check_min_heap([2, 10, 4, 5, 3, 15]) == False

check(check_min_heap_helper)