def is_polite(n):
    count = 0
    num = 1

    while count < n:
        num += 1
        if math.gcd(num, num - 1) == 1:
            count += 1

    return num

# Test cases




def check(candidate):
    assert is_polite(7) == 11
    assert is_polite(4) == 7
    assert is_polite(9) == 13

check(is_polite)