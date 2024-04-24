def get_max_sum(n):
    """
    Write a function to find the maximum sum possible by using the given equation f(n) = max((f(n/2) + f(n/3) + f(n/4) + f(n/5)), n).

    Examples:
    get_max_sum(60) == 106
    get_max_sum(10) == 12
    get_max_sum(2) == 2
    """
    if n <= 1:
        return n

    max_sum = n
    if n % 2 == 0:
        max_sum = max(max_sum, get_max_sum(n // 2))
    if n % 3 == 0:
        max_sum = max(max_sum, get_max_sum(n // 3))
    if n % 4 == 0:
        max_sum = max(max_sum, get_max_sum(n // 4))
    if n % 5 == 0:
        max_sum = max(max_sum, get_max_sum(n // 5))

    return max_sum

def check(candidate):
    assert get_max_sum(60) == 106
    assert get_max_sum(10) == 12
    assert get_max_sum(2) == 2

check(get_max_sum )