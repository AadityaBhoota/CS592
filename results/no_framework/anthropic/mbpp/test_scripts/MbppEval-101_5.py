def kth_element(arr, k, n):
    """
    Find the kth element in the given array using 1-based indexing.

    Args:
        arr (list): The input array.
        k (int): The desired 1-based index of the element to be found.
        n (int): The length of the input array.

    Returns:
        The kth element in the input array.
    """
    if k < 1 or k > n:
        raise ValueError("k must be within the range of the array length")

    arr.sort()
    return arr[k - 1]

def check(candidate):
    assert kth_element([12,3,5,7,19], 2) == 3
    assert kth_element([17,24,8,23], 3) == 8
    assert kth_element([16,21,25,36,4], 4) == 36

check(kth_element)