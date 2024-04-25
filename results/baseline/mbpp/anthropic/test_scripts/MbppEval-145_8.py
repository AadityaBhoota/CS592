def max_Abs_Diff(arr, n):
    """
    Find the maximum absolute difference between any two elements in a given array.
    
    Args:
        arr (list): The input array.
        n (int): The length of the array.
    
    Returns:
        int: The maximum absolute difference between any two elements in the array.
    """
    max_diff = 0
    
    for i in range(n):
        for j in range(i + 1, n):
            diff = abs(arr[i] - arr[j])
            if diff > max_diff:
                max_diff = diff
    
    return max_diff

def check(candidate):
    assert max_Abs_Diff((2,1,5,3)) == 4
    assert max_Abs_Diff((9,3,2,5,1)) == 8
    assert max_Abs_Diff((3,2,1)) == 2

check(max_Abs_Diff)