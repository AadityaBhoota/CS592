def is_equal_to_sum_even(n):
    if n < 8:
        return False

    for i in range(2, n // 2 + 1):
        for j in range(2, n // 2 + 1):
            for k in range(2, n // 2 + 1):
                for l in range(2, n // 2 + 1):
                    if i + j + k + l == n:
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