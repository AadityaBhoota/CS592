def find_star_num(n):
    """
    Write a function to find the n'th star number.

    Examples:
    find_star_num(3) == 37
    find_star_num(4) == 73
    find_star_num(5) == 121
    """
    return n * (3 * n - 1) // 2

def check(candidate):
    assert find_star_num(3) == 37
    assert find_star_num(4) == 73
    assert find_star_num(5) == 121

check(find_star_num)