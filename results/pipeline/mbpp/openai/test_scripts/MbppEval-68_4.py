def is_Monotonic(A):
    increasing = all(A[i] <= A[i + 1] for i in range(len(A) - 1))
    decreasing = all(A[i] >= A[i + 1] for i in range(len(A) - 1))
    
    if not (increasing or decreasing):
        return False
    
    return True

def check(candidate):
    assert is_Monotonic([6, 5, 4, 4]) == True
    assert is_Monotonic([1, 2, 2, 3]) == True
    assert is_Monotonic([1, 3, 2]) == False

check(is_Monotonic)