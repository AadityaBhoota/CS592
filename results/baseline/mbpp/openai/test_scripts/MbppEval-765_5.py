def is_polite(n):
    if n == 1:
        return 1
    p = 2
    while n > 1:
        p = p + 1
        count = 0
        for i in range(2, math.ceil(math.sqrt(p)) + 1):
            if p % i == 0:
                count += 1
                while p % i == 0:
                    p = p // i
        if p > 1:
            count += 1
        if count >= n:
            n -= 1
    return p

# Test cases




def check(candidate):
    assert is_polite(7) == 11
    assert is_polite(4) == 7
    assert is_polite(9) == 13

check(is_polite)