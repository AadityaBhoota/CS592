def is_equal_to_sum_even(n):
    even_numbers = [x for x in range(2, n) if x % 2 == 0]
    
    for a in even_numbers:
        for b in even_numbers:
            for c in even_numbers:
                for d in even_numbers:
                    if a + b + c + d == n:
                        return True
    return False

# Test cases




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