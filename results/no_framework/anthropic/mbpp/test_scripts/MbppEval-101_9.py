def kth_element(arr, n, k):
    """
    Find the kth element in the given array using 1-based indexing.

    Args:
        arr (list): The input array.
        n (int): The length of the array.
        k (int): The desired position of the element (1-based indexing).

    Returns:
        int: The kth element in the array.
    """
    arr.sort()  # Sort the array in ascending order
    return arr[k - 1]  # Return the (k-1)th element (1-based indexing)

def check(candidate):
    assert kth_element([12,3,5,7,19], 2) == 3
    assert kth_element([17,24,8,23], 3) == 8
    assert kth_element([16,21,25,36,4], 4) == 36

check(kth_element)