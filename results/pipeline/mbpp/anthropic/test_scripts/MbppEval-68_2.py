def is_Monotonic(A):
    increasing = True
    decreasing = True

    for i in range(1, len(A)):
        if A[i] > A[i - 1]:
            decreasing = False
        if A[i] < A[i - 1]:
            increasing = False

    return increasing or decreasing

def check(candidate):
    assert is_Monotonic([6, 5, 4, 4]) == True
    assert is_Monotonic([1, 2, 2, 3]) == True
    assert is_Monotonic([1, 3, 2]) == False

check(is_Monotonic)