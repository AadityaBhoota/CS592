def is_equal_to_sum_even(n):
    even_numbers = [x for x in range(n, 0, -2) if x % 2 == 0]
    
    for i in range(len(even_numbers)):
        for j in range(i+1, len(even_numbers)):
            for k in range(j+1, len(even_numbers)):
                for l in range(k+1, len(even_numbers)):
                    if even_numbers[i] + even_numbers[j] + even_numbers[k] + even_numbers[l] == n:
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