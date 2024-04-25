def last(arr, x, n):
    '''
    Write a python function to find the last position of an element in a sorted array.

    Examples:
    last([1,2,3],1,3) == 0
    last([1,1,1,2,3,4],1,6) == 2
    last([2,3,2,3,6,8,9],3,8) == 3

    Parameters:
    arr (list): A sorted list of integers.
    x (int): The element to search for in the list.
    n (int): The number of elements in the list.

    Returns:
    int: The last position of the element in the list. If the element is not found, return -1.
    '''
    index = -1

    for i in range(n - 1, -1, -1):
        if arr[i] == x:
            index = i
            break

    return index

def check(candidate):
    assert last([1,2,3],1) == 0
    assert last([1,1,1,2,3,4],1) == 2
    assert last([2,3,2,3,6,8,9],3) == 3

check(last)