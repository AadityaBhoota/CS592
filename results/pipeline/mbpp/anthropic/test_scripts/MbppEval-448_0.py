def cal_sum(n):
    """
    Write a function to calculate the sum of perrin numbers.

    Examples:
    cal_sum(9) == 49
    cal_sum(10) == 66
    cal_sum(11) == 88
    """
    perrin_nums = [0, 0, 2]
    
    if n <= 3:
        return sum(perrin_nums[:n])
    
    for i in range(3, n):
        next_num = perrin_nums[-3] + perrin_nums[-2]
        perrin_nums.append(next_num)
    
    return sum(perrin_nums[:n])

def check(candidate):
    assert cal_sum(9) == 49
    assert cal_sum(10) == 66
    assert cal_sum(11) == 88

check(cal_sum)