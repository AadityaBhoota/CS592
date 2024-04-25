def find_first_occurrence(A, x):
    left = 0
    right = len(A) - 1
    
    while left <= right:
        middle = (left + right) // 2
        
        if A[middle] == x:
            if middle == 0 or A[middle-1] != x:
                return middle
            else:
                right = middle - 1
        elif A[middle] < x:
            left = middle + 1
        else:
            right = middle - 1
    
    return -1

def check(candidate):
    assert find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 1
    assert find_first_occurrence([2, 3, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 2
    assert find_first_occurrence([2, 4, 1, 5, 6, 6, 8, 9, 9, 9], 6) == 4

check(find_first_occurrence)