def max_Abs_Diff(arr, n):
    """
    Find the maximum difference between any two elements in a given array.

    Args:
    arr (tuple): The input array.
    n (int): The length of the input array.

    Returns:
    int: The maximum absolute difference between any two elements in the array.
    """
    # Sort the array in ascending order
    arr = sorted(arr)

    # Initialize the maximum difference to 0
    max_diff = 0

    # Iterate through the sorted array and find the maximum difference
    for i in range(1, n):
        diff = abs(arr[i] - arr[i-1])
        if diff > max_diff:
            max_diff = diff

    return max_diff

def check(candidate):
    assert max_Abs_Diff((2,1,5,3)) == 4
    assert max_Abs_Diff((9,3,2,5,1)) == 8
    assert max_Abs_Diff((3,2,1)) == 2

check(max_Abs_Diff)