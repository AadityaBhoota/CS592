def count_rotation(arr):
    n = len(arr)
    start = 0
    end = n - 1

    while start <= end:
        if arr[start] <= arr[end]:
            return start  # No rotation needed
        mid = start + (end - start) // 2
        nextpos = (mid + 1) % n
        prevpos = (mid + n - 1) % n

        if arr[mid] <= arr[nextpos] and arr[mid] <= arr[prevpos]:
            return mid  # Found the pivot element
        elif arr[start] <= arr[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return 0  # Array is already sorted, no rotations needed

# Test cases




def check(candidate):
    assert count_rotation([3,2,1]) == 1
    assert count_rotation([4,5,1,2,3]) == 2
    assert count_rotation([7,8,9,1,2,3]) == 3
    assert count_rotation([1,2,3]) == 0
    assert count_rotation([1,3,2]) == 2

check(count_rotation)