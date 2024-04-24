def cal_sum(n):
    """
    Write a function to calculate the sum of Perrin numbers.

    Examples:
    cal_sum(9) == 49
    cal_sum(10) == 66
    cal_sum(11) == 88
    """
    if n <= 0:
        return 0

    perrin = [0, 0, 1]
    for i in range(3, n + 1):
        perrin.append(perrin[i - 2] + perrin[i - 3])

    return sum(perrin[:n + 1])

def check(candidate):
    assert cal_sum(9) == 49
    assert cal_sum(10) == 66
    assert cal_sum(11) == 88

check(cal_sum)