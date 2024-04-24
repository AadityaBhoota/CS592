def find_star_num(n):
    return n * (n + 1) + (n - 1) ** 2

# Test the function with the provided examples




def check(candidate):
    assert find_star_num(3) == 37
    assert find_star_num(4) == 73
    assert find_star_num(5) == 121

check(find_star_num)