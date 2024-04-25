def last(arr, x, n):
    """
    Find the last position of an element in a sorted array.

    Args:
        arr (list): The sorted array.
        x (int): The element to search for.
        n (int): The length of the array.

    Returns:
        int: The index of the last occurrence of the element, or -1 if not found.
    """
    left, right = 0, n - 1
    last_index = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            last_index = mid
            left = mid + 1
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return last_index

# Examples:




def check(candidate):
    assert last([1,2,3],1) == 0
    assert last([1,1,1,2,3,4],1) == 2
    assert last([2,3,2,3,6,8,9],3) == 3

check(last)