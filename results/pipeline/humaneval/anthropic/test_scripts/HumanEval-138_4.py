def is_equal_to_sum_even(n):
    if n % 4 != 0:
        return False
    
    a = 2
    while a <= n // 4:
        if n - a - (a + 2) - (a + 4) == 0:
            return True
        a += 2
    
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