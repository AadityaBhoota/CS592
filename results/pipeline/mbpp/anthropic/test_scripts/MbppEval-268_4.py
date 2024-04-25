def find_star_num(n):
    total = 0
    for i in range(1, 2*n, 2):
        total += i
    return total

def check(candidate):
    assert find_star_num(3) == 37
    assert find_star_num(4) == 73
    assert find_star_num(5) == 121

check(find_star_num)