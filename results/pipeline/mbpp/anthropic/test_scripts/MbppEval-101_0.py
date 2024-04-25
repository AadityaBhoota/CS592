def kth_element(arr, k):
    """
    Find the kth element in the given array using 1-based indexing.
    
    Args:
        arr (list): The input array.
        k (int): The 1-based index of the element to find.
        
    Returns:
        The kth element of the array.
        
    Raises:
        ValueError: If k is not within the valid range of the array size (1 <= k <= len(arr)).
    """
    if k < 1 or k > len(arr):
        raise ValueError("k is not within the valid range of the array size (1 <= k <= len(arr))")
    return arr[k-1]

def check(candidate):
    assert kth_element([12,3,5,7,19], 2) == 3
    assert kth_element([17,24,8,23], 3) == 8
    assert kth_element([16,21,25,36,4], 4) == 36

check(kth_element)