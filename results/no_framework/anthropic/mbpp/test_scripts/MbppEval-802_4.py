def count_rotation(arr):
    """
    Counts the number of rotations required to generate a sorted array.
    
    Args:
        arr (list): The input array.
        
    Returns:
        int: The number of rotations required to generate a sorted array.
    """
    if not arr:
        return 0
    
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = left + (right - left) // 2
        
        # If the middle element is greater than the rightmost element,
        # then the rotations lie in the left half.
        if arr[mid] > arr[right]:
            left = mid + 1
        else:
            right = mid
    
    return left

def check(candidate):
    assert count_rotation([3,2,1]) == 1
    assert count_rotation([4,5,1,2,3]) == 2
    assert count_rotation([7,8,9,1,2,3]) == 3
    assert count_rotation([1,2,3]) == 0
    assert count_rotation([1,3,2]) == 2

check(count_rotation)