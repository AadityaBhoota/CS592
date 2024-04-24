def is_polite(n):
    polite_count = 1
    curr_num = 1
    while polite_count < n:
        curr_num += 1
        if math.gcd(curr_num, polite_count) == 1:
            polite_count += 1
    return curr_num

# Test cases




def check(candidate):
    assert is_polite(7) == 11
    assert is_polite(4) == 7
    assert is_polite(9) == 13

check(is_polite)