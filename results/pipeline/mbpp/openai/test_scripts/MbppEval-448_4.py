def cal_sum(n):
    def perrin_number(n):
        if n == 0:
            return 3
        elif n == 1:
            return 0
        elif n == 2:
            return 2
        else:
            return perrin_number(n-2) + perrin_number(n-3)
    
    if n <= 0:
        return 0
    
    perrin_sum = 0
    for i in range(n):
        perrin_sum += perrin_number(i)
    
    return perrin_sum

def check(candidate):
    assert cal_sum(9) == 49
    assert cal_sum(10) == 66
    assert cal_sum(11) == 88

check(cal_sum)