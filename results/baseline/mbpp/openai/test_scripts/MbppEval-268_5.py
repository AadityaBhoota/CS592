def find_star_num(n): 
    if n == 1:
        return 3
    else:
        return find_star_num(n - 1) + 10*(n-1)

def check(candidate):
    assert find_star_num(3) == 37
    assert find_star_num(4) == 73
    assert find_star_num(5) == 121

check(find_star_num)