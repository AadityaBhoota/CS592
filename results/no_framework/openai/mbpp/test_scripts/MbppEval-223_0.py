def is_majority(arr, n, x):
    # Find the first occurrence index of x using binary search
    def first_occurrence(arr, x):
        left, right = 0, len(arr) - 1
        result = -1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == x:
                result = mid
                right = mid - 1
            elif arr[mid] < x:
                left = mid + 1
            else:
                right = mid - 1
        return result

    # Find the last occurrence index of x using binary search
    def last_occurrence(arr, x):
        left, right = 0, len(arr) - 1
        result = -1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == x:
                result = mid
                left = mid + 1
            elif arr[mid] < x:
                left = mid + 1
            else:
                right = mid - 1
        return result

    first_index = first_occurrence(arr, x)
    last_index = last_occurrence(arr, x)

    # Check if the element occurs more than n/2 times
    if first_index != -1 and last_index != -1:
        return (last_index - first_index + 1) > n / 2
    return False

# Test cases




def check(candidate):
    assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True
    assert is_majority([1, 1, 2, 4, 4, 4, 6, 6], 8, 4) == False
    assert is_majority([1, 1, 1, 2, 2], 5, 1) == True
    assert is_majority([1, 1, 2, 2], 5, 1) == False

check(is_majority)