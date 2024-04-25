def count_rotation(arr):
    """
    Counts the number of rotations required to generate a sorted array.

    Args:
        arr (list): The input array.

    Returns:
        int: The number of rotations required.
    """
    n = len(arr)
    left, right = 0, n - 1

    while left <= right:
        if arr[left] <= arr[right]:
            return left
        mid = (left + right) // 2
        prev = (mid - 1) % n
        next = (mid + 1) % n

        if arr[mid] <= arr[prev] and arr[mid] <= arr[next]:
            return mid
        elif arr[mid] <= arr[right]:
            right = mid - 1
        else:
            left = mid + 1

    return 0

def check(candidate):
    assert count_rotation([3,2,1]) == 1
    assert count_rotation([4,5,1,2,3]) == 2
    assert count_rotation([7,8,9,1,2,3]) == 3
    assert count_rotation([1,2,3]) == 0
    assert count_rotation([1,3,2]) == 2

check(count_rotation)