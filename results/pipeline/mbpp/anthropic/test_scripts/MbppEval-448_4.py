def cal_sum(n):
    """
    Write a function to calculate the sum of perrin numbers.

    Examples:
    cal_sum(9) == 49
    cal_sum(10) == 66
    cal_sum(11) == 88
    """
    perrin = [3, 0, 2]
    for i in range(3, n):
        next_perrin = perrin[-3] + perrin[-2]
        perrin.append(next_perrin)
    return sum(perrin)

def check(candidate):
    assert cal_sum(9) == 49
    assert cal_sum(10) == 66
    assert cal_sum(11) == 88

check(cal_sum)