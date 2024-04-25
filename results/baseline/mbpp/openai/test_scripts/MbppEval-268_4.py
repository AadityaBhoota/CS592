def find_star_num(n):
    star_num = 6 * n * (n - 1) + 1
    return star_num

# Test cases




def check(candidate):
    assert find_star_num(3) == 37
    assert find_star_num(4) == 73
    assert find_star_num(5) == 121

check(find_star_num)