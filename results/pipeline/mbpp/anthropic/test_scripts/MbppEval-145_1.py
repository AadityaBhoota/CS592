def max_Abs_Diff(arr):
    """
    Find the maximum difference between any two elements in a given array.

    Args:
        arr (list): The input array.

    Returns:
        int: The maximum absolute difference between any two elements in the array.
    """
    max_val = max(arr)
    min_val = min(arr)
    return abs(max_val - min_val)

def check(candidate):
    assert max_Abs_Diff((2,1,5,3)) == 4
    assert max_Abs_Diff((9,3,2,5,1)) == 8
    assert max_Abs_Diff((3,2,1)) == 2

check(max_Abs_Diff)