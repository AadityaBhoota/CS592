def perrin(n):
    if n == 0:
        return 3
    if n == 1:
        return 0
    if n == 2:
        return 2
    return perrin(n-2) + perrin(n-3)

def cal_sum(n):
    total_sum = 0
    for i in range(n + 1):
        total_sum += perrin(i)
    return total_sum

def check(candidate):
    assert cal_sum(9) == 49
    assert cal_sum(10) == 66
    assert cal_sum(11) == 88

check(cal_sum)