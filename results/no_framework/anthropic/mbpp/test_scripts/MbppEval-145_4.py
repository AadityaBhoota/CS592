def max_Abs_Diff(arr, n):
    """
    Find the maximum absolute difference between any two elements in the given array.

    Args:
        arr (list): The input array.
        n (int): The length of the array.

    Returns:
        int: The maximum absolute difference.
    """
    # Initialize the maximum difference to 0
    max_diff = 0

    # Iterate through the array
    for i in range(n):
        for j in range(i + 1, n):
            # Calculate the absolute difference between the current elements
            diff = abs(arr[i] - arr[j])
            # Update the maximum difference if the current difference is greater
            max_diff = max(max_diff, diff)

    return max_diff

def check(candidate):
    assert max_Abs_Diff((2,1,5,3)) == 4
    assert max_Abs_Diff((9,3,2,5,1)) == 8
    assert max_Abs_Diff((3,2,1)) == 2

check(max_Abs_Diff)