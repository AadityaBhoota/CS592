def get_max_sum(n, memo={}):
    if n <= 1:
        return n

    if n in memo:
        return memo[n]

    sum_val = max(n, get_max_sum(n//2, memo) + get_max_sum(n//3, memo) + get_max_sum(n//4, memo) + get_max_sum(n//5, memo))
    memo[n] = sum_val

    return sum_val

# Test cases




def check(candidate):
    assert get_max_sum(60) == 106
    assert get_max_sum(10) == 12
    assert get_max_sum(2) == 2

check(get_max_sum )