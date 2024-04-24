def perrin(n):
    p0, p1, p2 = 3, 0, 2
    perrin_sum = 0
    for i in range(3, n + 1):
        pn = p0 + p1
        perrin_sum += pn
        p0, p1, p2 = p1, p2, pn
    return perrin_sum

def cal_sum(n):
    return perrin(n)

# Test cases




def check(candidate):
    assert cal_sum(9) == 49
    assert cal_sum(10) == 66
    assert cal_sum(11) == 88

check(cal_sum)