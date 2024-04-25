def count_rotation(arr, n):
    left, right = 0, n - 1

    while left <= right:
        # If the array is already sorted, return 0 rotations
        if arr[left] <= arr[right]:
            return left

        mid = (left + right) // 2
        prev = (mid + n - 1) % n
        next = (mid + 1) % n

        # Check if mid is the rotation point
        if arr[mid] <= arr[prev] and arr[mid] <= arr[next]:
            return mid

        # Move search to the unsorted side of the array
        if arr[mid] <= arr[right]:
            right = mid - 1
        elif arr[left] <= arr[mid]:
            left = mid + 1

    return 0

# Test cases




def check(candidate):
    assert count_rotation([3,2,1]) == 1
    assert count_rotation([4,5,1,2,3]) == 2
    assert count_rotation([7,8,9,1,2,3]) == 3
    assert count_rotation([1,2,3]) == 0
    assert count_rotation([1,3,2]) == 2

check(count_rotation)