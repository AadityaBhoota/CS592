def find_star_num(n):
    result = 1
    while n > 0:
        result += 2
        n -= 1
    return result

def check(candidate):
    assert find_star_num(3) == 37
    assert find_star_num(4) == 73
    assert find_star_num(5) == 121

check(find_star_num)