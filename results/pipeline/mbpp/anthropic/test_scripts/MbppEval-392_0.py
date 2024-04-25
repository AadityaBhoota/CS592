def get_max_sum (n):
    '''
    Write a function to find the maximum sum possible by using the given equation f(n) = max( (f(n/2) + f(n/3) + f(n/4) + f(n/5)), n).

    Examples:
    get_max_sum(60) == 106
    get_max_sum(10) == 12
    get_max_sum(2) == 2
    '''
def get_max_sum(n):
    if n <= 1:
        return n

    memo = {1: 1, 2: 2}

    for i in range(3, n + 1):
        max_sum = i
        for div in (2, 3, 4, 5):
            if i % div == 0:
                max_sum = max(max_sum, memo[i // div] + i // div)
        memo[i] = max_sum

    return memo[n]

def check(candidate):
    assert get_max_sum(60) == 106
    assert get_max_sum(10) == 12
    assert get_max_sum(2) == 2

check(get_max_sum )