def get_max_sum (n):
    '''
    Write a function to find the maximum sum possible by using the given equation f(n) = max( (f(n/2) + f(n/3) + f(n/4) + f(n/5)), n).

    Examples:
    get_max_sum(60) == 106
    get_max_sum(10) == 12
    get_max_sum(2) == 2
    '''
def get_max_sum(n, memo={}):
    if n in memo:
        return memo[n]

    if n == 0:
        return 0

    max_sum = max(n, get_max_sum(n//2, memo) + get_max_sum(n//3, memo) + get_max_sum(n//4, memo) + get_max_sum(n//5, memo))
    memo[n] = max_sum

    return max_sum

# Test cases




def check(candidate):
    assert get_max_sum(60) == 106
    assert get_max_sum(10) == 12
    assert get_max_sum(2) == 2

check(get_max_sum )