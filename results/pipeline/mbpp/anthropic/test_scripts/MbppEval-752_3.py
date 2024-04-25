def jacobsthal_num(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        j0 = 0
        j1 = 1
        for i in range(2, n+1):
            j2 = j1 + 2 * j0
            j0 = j1
            j1 = j2
        return j1

def check(candidate):
    assert jacobsthal_num(5) == 11
    assert jacobsthal_num(2) == 1
    assert jacobsthal_num(4) == 5
    assert jacobsthal_num(13) == 2731

check(jacobsthal_num)