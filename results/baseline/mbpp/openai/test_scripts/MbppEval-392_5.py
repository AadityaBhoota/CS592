def get_max_sum (n):
    '''
    Write a function to find the maximum sum possible by using the given equation f(n) = max( (f(n/2) + f(n/3) + f(n/4) + f(n/5)), n).

    Examples:
    get_max_sum(60) == 106
    get_max_sum(10) == 12
    get_max_sum(2) == 2
    '''
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