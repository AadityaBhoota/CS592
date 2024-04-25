def sum(a, b):
    common_divisors_list = common_divisors(a, b)
    return sum(common_divisors_list)

def check(candidate):
    assert sum(10,15) == 6
    assert sum(100,150) == 93
    assert sum(4,6) == 3

check(sum)