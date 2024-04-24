def last(arr, x, n):
    '''
    Find the last position of an element in a sorted array.

    Args:
    arr (List[int]): The sorted array to search in.
    x (int): The target element to find.
    n (int): The length of the array.

    Returns:
    int: The last position of the target element in the array, or -1 if the element is not found.
    '''
    start = 0
    end = n - 1
    result = -1

    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == x:
            result = mid
            start = mid + 1
        elif arr[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
    
    return result

# Test the function




def check(candidate):
    assert last([1,2,3],1) == 0
    assert last([1,1,1,2,3,4],1) == 2
    assert last([2,3,2,3,6,8,9],3) == 3

check(last)