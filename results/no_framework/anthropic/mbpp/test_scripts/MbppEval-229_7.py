def re_arrange_array(arr, n):
    """
    Rearrange the first n elements of the given array such that all negative elements appear before positive ones, while preserving the relative order.
    
    Args:
    arr (list): The input array.
    n (int): The number of elements to rearrange.
    
    Returns:
    list: The rearranged array.
    """
    # Create two lists to store negative and positive elements
    negative = []
    positive = []
    
    # Iterate through the first n elements of the array
    for i in range(n):
        if arr[i] < 0:
            negative.append(arr[i])
        else:
            positive.append(arr[i])
    
    # Combine the negative and positive elements in the correct order
    rearranged = negative + positive
    
    # Return the rearranged array
    return rearranged

def check(candidate):
    assert re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 9) == [-1, -3, -7, 4, 5, 6, 2, 8, 9]
    assert re_arrange_array([12, -14, -26, 13, 15], 5) == [-14, -26, 12, 13, 15]
    assert re_arrange_array([10, 24, 36, -42, -39, -78, 85], 7) == [-42, -39, -78, 10, 24, 36, 85]

check(re_arrange_array)