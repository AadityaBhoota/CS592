def cal_sum(n):
    """
    Write a function to calculate the sum of perrin numbers.

    Examples:
    cal_sum(9) == 49
    cal_sum(10) == 66
    cal_sum(11) == 88
    """
    if n < 1:
        return 0

    perrin_sequence = [3, 0, 2]
    for i in range(3, n+1):
        perrin_sequence.append(perrin_sequence[i-2] + perrin_sequence[i-3])

    return sum(perrin_sequence[:n+1])

def check(candidate):
    assert cal_sum(9) == 49
    assert cal_sum(10) == 66
    assert cal_sum(11) == 88

check(cal_sum)