def find_First_Missing(array, start=0, end=None):
    if end is None:
        end = len(array) - 1

    # Check if the array is empty or the first element is not 0
    if len(array) == 0 or array[0] != 0:
        return 0

    # Check if the last element is present in the array
    if array[-1] != end:
        return end

    # Perform binary search to find the missing number
    while start <= end:
        mid = start + (end - start) // 2

        if array[mid] > mid:
            end = mid - 1
        else:
            start = mid + 1

    return start

# Test cases




def check(candidate):
    assert find_First_Missing([0,1,2,3]) == 4
    assert find_First_Missing([0,1,2,6,9]) == 3
    assert find_First_Missing([2,3,5,8,9]) == 0

check(find_First_Missing)