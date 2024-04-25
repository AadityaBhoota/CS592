def find_star_num(n):
    return n**3 + 6*n**2 + 11*n + 6

def check(candidate):
    assert find_star_num(3) == 37
    assert find_star_num(4) == 73
    assert find_star_num(5) == 121

check(find_star_num)