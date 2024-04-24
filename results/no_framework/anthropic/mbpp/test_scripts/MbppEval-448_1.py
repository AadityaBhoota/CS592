def cal_sum(n):
    """
    Write a function to calculate the sum of Perrin numbers.

    Examples:
    cal_sum(9) == 49
    cal_sum(10) == 66
    cal_sum(11) == 88
    """
    if n < 1:
        return 0

    # Initialize the Perrin sequence
    p = [0, 0, 1]

    # Compute the Perrin sequence up to the given n
    for i in range(3, n+1):
        p.append(p[i-2] + p[i-3])

    # Calculate the sum of the Perrin numbers
    return sum(p[:n+1])

def check(candidate):
    assert cal_sum(9) == 49
    assert cal_sum(10) == 66
    assert cal_sum(11) == 88

check(cal_sum)