def is_Monotonic(A):
    if not A:
        return True

    increasing = decreasing = True

    for i in range(len(A) - 1):
        if A[i] < A[i+1]:
            decreasing = False
        if A[i] > A[i+1]:
            increasing = False

        if not increasing and not decreasing:
            return False

    return increasing or decreasing

def check(candidate):
    assert is_Monotonic([6, 5, 4, 4]) == True
    assert is_Monotonic([1, 2, 2, 3]) == True
    assert is_Monotonic([1, 3, 2]) == False

check(is_Monotonic)