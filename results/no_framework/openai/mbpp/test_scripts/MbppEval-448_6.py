def perrin(n):
    if n == 0:
        return 3
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        return perrin(n-2) + perrin(n-3)

def cal_sum(n):
    total = 0
    for i in range(n):
        total += perrin(i)
    return total

# Test cases




def check(candidate):
    assert cal_sum(9) == 49
    assert cal_sum(10) == 66
    assert cal_sum(11) == 88

check(cal_sum)