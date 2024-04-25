def find_first_occurrence(A, x):
    left, right = 0, len(A) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2
        
        if A[mid] == x:
            result = mid
            right = mid - 1
        elif A[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return result

def check(candidate):
    assert find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 1
    assert find_first_occurrence([2, 3, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 2
    assert find_first_occurrence([2, 4, 1, 5, 6, 6, 8, 9, 9, 9], 6) == 4

check(find_first_occurrence)