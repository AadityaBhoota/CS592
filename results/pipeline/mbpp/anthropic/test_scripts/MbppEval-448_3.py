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

    # Initialize the first three Perrin numbers
    perrin = [3, 0, 2]

    # Calculate the Perrin numbers up to the nth term
    for i in range(3, n):
        next_perrin = perrin[i-3] + perrin[i-2] + perrin[i-1]
        perrin.append(next_perrin)

    # Calculate the sum of the Perrin numbers
    return sum(perrin)

def check(candidate):
    assert cal_sum(9) == 49
    assert cal_sum(10) == 66
    assert cal_sum(11) == 88

check(cal_sum)