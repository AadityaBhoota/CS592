def kth_element(arr, n, k):
    """
    Write a function to find the kth element in the given array using 1-based indexing.

    Args:
        arr (list): The input array.
        n (int): The length of the input array.
        k (int): The k-th element to find.

    Returns:
        int: The k-th element in the input array.
    """
    # Sort the array in ascending order
    arr.sort()

    # Return the (k-1)th element (since indexing starts from 0)
    return arr[k-1]

def check(candidate):
    assert kth_element([12,3,5,7,19], 2) == 3
    assert kth_element([17,24,8,23], 3) == 8
    assert kth_element([16,21,25,36,4], 4) == 36

check(kth_element)