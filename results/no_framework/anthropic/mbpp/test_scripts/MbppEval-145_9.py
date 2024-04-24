def max_Abs_Diff(arr, n):
    """
    Write a python function to find the maximum difference between any two elements in a given array.

    Args:
        arr (list): The input array.
        n (int): The length of the input array.

    Returns:
        int: The maximum absolute difference between any two elements in the array.
    """
    if n < 2:
        return 0

    max_diff = 0
    for i in range(n):
        for j in range(i + 1, n):
            max_diff = max(max_diff, abs(arr[i] - arr[j]))

    return max_diff

def check(candidate):
    assert max_Abs_Diff((2,1,5,3)) == 4
    assert max_Abs_Diff((9,3,2,5,1)) == 8
    assert max_Abs_Diff((3,2,1)) == 2

check(max_Abs_Diff)