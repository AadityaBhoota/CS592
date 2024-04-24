def is_Monotonic(A):
    """
    Write a python function to check whether the given array is monotonic or not.

    Examples:
    is_Monotonic([6, 5, 4, 4]) == True
    is_Monotonic([1, 2, 2, 3]) == True
    is_Monotonic([1, 3, 2]) == False
    """
    # Check if the array is non-decreasing
    is_non_decreasing = all(A[i] <= A[i+1] for i in range(len(A)-1))
    
    # Check if the array is non-increasing
    is_non_increasing = all(A[i] >= A[i+1] for i in range(len(A)-1))
    
    # Return True if the array is monotonic, False otherwise
    return is_non_decreasing or is_non_increasing

def check(candidate):
    assert is_Monotonic([6, 5, 4, 4]) == True
    assert is_Monotonic([1, 2, 2, 3]) == True
    assert is_Monotonic([1, 3, 2]) == False

check(is_Monotonic)