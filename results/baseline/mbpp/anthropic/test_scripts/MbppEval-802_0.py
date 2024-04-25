def count_rotation(arr):
    """
    Write a python function to count the number of rotations required to generate a sorted array.
    Examples:
    count_Rotation([3,2,1],3) == 1
    count_Rotation([4,5,1,2,3],5) == 2
    count_Rotation([7,8,9,1,2,3],6) == 3
    """
    if not arr:
        return 0

    left, right = 0, len(arr) - 1

    while left < right:
        mid = left + (right - left) // 2

        # If the middle element is greater than the rightmost element, then the rotations lie in the left half
        if arr[mid] > arr[right]:
            left = mid + 1
        else:
            right = mid

    return left

# Examples:




def check(candidate):
    assert count_rotation([3,2,1]) == 1
    assert count_rotation([4,5,1,2,3]) == 2
    assert count_rotation([7,8,9,1,2,3]) == 3
    assert count_rotation([1,2,3]) == 0
    assert count_rotation([1,3,2]) == 2

check(count_rotation)