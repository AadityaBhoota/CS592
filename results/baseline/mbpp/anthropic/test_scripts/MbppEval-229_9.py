def re_arrange_array(arr, n):
    """
    Rearranges the first n elements of the given array so that all negative elements appear before positive ones, while preserving the relative order among negative and positive elements.
    """
    # Create two separate lists to hold negative and positive elements
    negative = []
    positive = []
    
    # Iterate through the first n elements of the array
    for i in range(n):
        # If the element is negative, add it to the negative list
        if arr[i] < 0:
            negative.append(arr[i])
        # Otherwise, add it to the positive list
        else:
            positive.append(arr[i])
    
    # Combine the negative and positive lists, preserving the relative order
    result = negative + positive
    
    return result

def check(candidate):
    assert re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 9) == [-1, -3, -7, 4, 5, 6, 2, 8, 9]
    assert re_arrange_array([12, -14, -26, 13, 15], 5) == [-14, -26, 12, 13, 15]
    assert re_arrange_array([10, 24, 36, -42, -39, -78, 85], 7) == [-42, -39, -78, 10, 24, 36, 85]

check(re_arrange_array)