def perrin(n):
    if n == 0:
        return 3
    if n == 1:
        return 0
    if n == 2:
        return 2
    p = [3, 0, 2]
    for i in range(3, n+1):
        p.append(p[i-2] + p[i-3])
    return sum(p)

def cal_sum(n):
    return perrin(n-1)

# Test cases




def check(candidate):
    assert cal_sum(9) == 49
    assert cal_sum(10) == 66
    assert cal_sum(11) == 88

check(cal_sum)