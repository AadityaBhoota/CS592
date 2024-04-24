def find_lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        lucas_n_minus_1 = 1
        lucas_n_minus_2 = 2
        for i in range(2, n+1):
            lucas_n = lucas_n_minus_1 + lucas_n_minus_2
            lucas_n_minus_1, lucas_n_minus_2 = lucas_n, lucas_n_minus_1
        return lucas_n

# Test cases




def check(candidate):
    assert find_lucas(9) == 76
    assert find_lucas(4) == 7
    assert find_lucas(3) == 4

check(find_lucas)