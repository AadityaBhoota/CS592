def find_lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        lucas_prev, lucas_current = 2, 1
        for _ in range(2, n+1):
            lucas_next = lucas_prev + lucas_current
            lucas_prev, lucas_current = lucas_current, lucas_next
        return lucas_current

# Test cases




def check(candidate):
    assert find_lucas(9) == 76
    assert find_lucas(4) == 7
    assert find_lucas(3) == 4

check(find_lucas)