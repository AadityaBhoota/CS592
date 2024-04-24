def count_rotation(arr, n):
    # Function to count the number of rotations required to generate a sorted array
    
    # Find the pivot element using binary search
    def find_pivot(arr, low, high):
        if high < low:
            return -1
        if high == low:
            return low
        
        mid = (low + high) // 2
        
        if mid < high and arr[mid] > arr[mid + 1]:
            return mid
        if mid > low and arr[mid] < arr[mid - 1]:
            return mid - 1
        
        if arr[low] >= arr[mid]:
            return find_pivot(arr, low, mid - 1)
        return find_pivot(arr, mid + 1, high)
    
    pivot = find_pivot(arr, 0, n - 1)
    
    return pivot + 1

# Test cases




def check(candidate):
    assert count_rotation([3,2,1]) == 1
    assert count_rotation([4,5,1,2,3]) == 2
    assert count_rotation([7,8,9,1,2,3]) == 3
    assert count_rotation([1,2,3]) == 0
    assert count_rotation([1,3,2]) == 2

check(count_rotation)