def jacobsthal_num(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return jacobsthal_num(n - 1) + 2 * jacobsthal_num(n - 2)

# Test cases




def check(candidate):
    assert jacobsthal_num(5) == 11
    assert jacobsthal_num(2) == 1
    assert jacobsthal_num(4) == 5
    assert jacobsthal_num(13) == 2731

check(jacobsthal_num)