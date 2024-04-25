def perrin_number(n):
    if n == 0:
        return 3
    if n == 1:
        return 0
    if n == 2:
        return 2
    else:
        return perrin_number(n-2) + perrin_number(n-3)

def cal_sum(n):
    if n <= 0:
        return 0
    
    perrin_numbers = [perrin_number(i) for i in range(n)]
    return sum(perrin_numbers)

# Test cases




def check(candidate):
    assert cal_sum(9) == 49
    assert cal_sum(10) == 66
    assert cal_sum(11) == 88

check(cal_sum)