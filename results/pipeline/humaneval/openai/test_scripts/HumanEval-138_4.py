def is_equal_to_sum_even(n):
    if n < 8:
        return False

    if n % 4 == 0:
        return True
    
    for i in range(2, n-6, 2):
        for j in range(i, n-4, 2):
            for k in range(j, n-2, 2):
                if i + j + k + n == n:
                    return True
                
    return False

def check(candidate):
    assert candidate(4) == False
    assert candidate(6) == False
    assert candidate(8) == True
    assert candidate(10) == True
    assert candidate(11) == False
    assert candidate(12) == True
    assert candidate(13) == False
    assert candidate(16) == True

check(is_equal_to_sum_even)