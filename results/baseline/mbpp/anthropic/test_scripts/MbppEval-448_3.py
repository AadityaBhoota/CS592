def cal_sum(n):
    """
    Write a function to calculate the sum of Perrin numbers.

    The Perrin sequence is a sequence of integers, similar to the Fibonacci sequence,
    defined by the recurrence relation: P(n) = P(n-2) + P(n-3), with the initial conditions:
    P(0) = 3, P(1) = 0, and P(2) = 2.

    Examples:
    cal_sum(9) == 49
    cal_sum(10) == 66
    cal_sum(11) == 88
    """
    if n <= 0:
        return 0
    
    perrin = [3, 0, 2]
    for i in range(3, n):
        perrin.append(perrin[-2] + perrin[-3])
    
    return sum(perrin[:n])

def check(candidate):
    assert cal_sum(9) == 49
    assert cal_sum(10) == 66
    assert cal_sum(11) == 88

check(cal_sum)