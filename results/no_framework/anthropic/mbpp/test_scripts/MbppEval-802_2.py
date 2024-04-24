def count_rotation(arr):
    """
    Write a python function to count the number of rotations required to generate a sorted array.
    """
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = left + (right - left) // 2

        # If the middle element is greater than the last element, then
        # the pivot element lies in the right half.
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