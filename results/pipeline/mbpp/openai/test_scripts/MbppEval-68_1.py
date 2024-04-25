def is_Monotonic(A):
    inc = dec = False
    
    for i in range(1, len(A)):
        if A[i] > A[i - 1]:
            inc = True
        elif A[i] < A[i - 1]:
            dec = True
            
        if inc and dec:
            return False
        
    return True

def check(candidate):
    assert is_Monotonic([6, 5, 4, 4]) == True
    assert is_Monotonic([1, 2, 2, 3]) == True
    assert is_Monotonic([1, 3, 2]) == False

check(is_Monotonic)