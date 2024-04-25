def is_Monotonic(A):
    """
    Determine if a given array is monotonic.
    
    An array is monotonic if it is either monotonically increasing or monotonically decreasing.
    
    Args:
        A (list): The input array to be checked.
        
    Returns:
        bool: True if the array is monotonic, False otherwise.
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