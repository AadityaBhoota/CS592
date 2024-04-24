def count_rotation(arr):
    """
    Write a python function to count the number of rotations required to generate a sorted array.
    
    Args:
        arr (list): The input list of integers.
        
    Returns:
        int: The number of rotations required to generate a sorted array.
    """
    low = 0
    high = len(arr) - 1
    
    while low < high:
        mid = low + (high - low) // 2
        
        # If the middle element is greater than the last element, then
        # the pivot element lies in the right half.
        if arr[mid] > arr[high]:
            low = mid + 1
        else:
            high = mid
    
    # The low index will be pointing to the smallest element, which is the
    # number of rotations.
    return low

def check(candidate):
    assert count_rotation([3,2,1]) == 1
    assert count_rotation([4,5,1,2,3]) == 2
    assert count_rotation([7,8,9,1,2,3]) == 3
    assert count_rotation([1,2,3]) == 0
    assert count_rotation([1,3,2]) == 2

check(count_rotation)