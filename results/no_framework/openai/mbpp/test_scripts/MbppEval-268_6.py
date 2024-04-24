def find_star_num(n):
    star_num = 0
    if n > 0:
        star_num = int('7' + '3'*(n-1))
    return star_num

# Test cases




def check(candidate):
    assert find_star_num(3) == 37
    assert find_star_num(4) == 73
    assert find_star_num(5) == 121

check(find_star_num)