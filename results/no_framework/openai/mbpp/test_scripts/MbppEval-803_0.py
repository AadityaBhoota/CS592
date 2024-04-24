def is_perfect_square(n):
    if n < 0:
        return False
    if n == 0:
        return True
    x = n // 2
    seen = set()
    while x * x != n:
        x = (x + n // x) // 2
        if x in seen:
            return False
        seen.add(x)
    return True

# Test cases




def check(candidate):
    assert not is_perfect_square(10)
    assert is_perfect_square(36)
    assert not is_perfect_square(14)
    assert is_perfect_square(14*14)
    assert not is_perfect_square(125)
    assert is_perfect_square(125*125)

check(is_perfect_square)