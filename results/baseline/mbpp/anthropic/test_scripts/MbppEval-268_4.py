def find_star_num(n):
    """
    Write a function to find the n'th star number.

    Examples:
    find_star_num(3) == 37
    find_star_num(4) == 73
    find_star_num(5) == 121
    """
    if n < 1:
        return 0
    return 2 * n * (n - 1) + 1

def check(candidate):
    assert find_star_num(3) == 37
    assert find_star_num(4) == 73
    assert find_star_num(5) == 121

check(find_star_num)