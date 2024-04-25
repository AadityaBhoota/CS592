def is_Monotonic(A):
    """
    Check whether the given array is monotonic or not.

    Args:
        A (list): The input list to be checked.

    Returns:
        bool: True if the list is monotonic, False otherwise.
    """
    is_increasing = True
    is_decreasing = True

    for i in range(1, len(A)):
        if A[i] > A[i-1]:
            is_decreasing = False
        if A[i] < A[i-1]:
            is_increasing = False

    return is_increasing or is_decreasing

def check(candidate):
    assert is_Monotonic([6, 5, 4, 4]) == True
    assert is_Monotonic([1, 2, 2, 3]) == True
    assert is_Monotonic([1, 3, 2]) == False

check(is_Monotonic)