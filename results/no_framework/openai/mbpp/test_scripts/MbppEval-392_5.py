def get_max_sum(n):
    if n == 0:
        return 0

    memo = {}

    def helper(n):
        if n in memo:
            return memo[n]

        if n == 1:
            memo[n] = 1
        else:
            memo[n] = max(helper(n//2) + helper(n//3) + helper(n//4) + helper(n//5), n)

        return memo[n]

    return helper(n)

# Test cases




def check(candidate):
    assert get_max_sum(60) == 106
    assert get_max_sum(10) == 12
    assert get_max_sum(2) == 2

check(get_max_sum )