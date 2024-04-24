def re_arrange_array(arr, n):
    """
    Rearranges the first n elements of the given array so that all negative elements appear before positive ones, and the relative order among negative and positive elements is preserved.
    """
    # Divide the array into negative and positive parts
    negative = [x for x in arr[:n] if x < 0]
    positive = [x for x in arr[:n] if x >= 0]
    
    # Combine the negative and positive parts back into the original array
    result = negative + positive
    result.extend(arr[n:])
    
    return result

def check(candidate):
    assert re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 9) == [-1, -3, -7, 4, 5, 6, 2, 8, 9]
    assert re_arrange_array([12, -14, -26, 13, 15], 5) == [-14, -26, 12, 13, 15]
    assert re_arrange_array([10, 24, 36, -42, -39, -78, 85], 7) == [-42, -39, -78, 10, 24, 36, 85]

check(re_arrange_array)