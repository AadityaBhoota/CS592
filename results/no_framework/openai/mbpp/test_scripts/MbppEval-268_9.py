def find_star_num(n):
    if n == 1:
        return 1
    num = 2
    for _ in range(2, n + 1):
        num = int(str(num) + str(num)[-1]) + 1
    return num

# Test cases




def check(candidate):
    assert find_star_num(3) == 37
    assert find_star_num(4) == 73
    assert find_star_num(5) == 121

check(find_star_num)