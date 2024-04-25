def last(arr, x, n):
    '''
    Find the last position of an element in a sorted array.

    Parameters:
    arr (list): Sorted array
    x (int): Element to find
    n (int): Size of the array

    Returns:
    int: Last position of the element in the array
    '''
    low = 0
    high = n - 1
    result = -1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == x:
            result = mid
            low = mid + 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return result

def check(candidate):
    assert last([1,2,3],1) == 0
    assert last([1,1,1,2,3,4],1) == 2
    assert last([2,3,2,3,6,8,9],3) == 3

check(last)