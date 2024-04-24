def bell_number(n):
    """
    Calculates the nth Bell number.

    The Bell number B(n) is the number of different partitions of a set of n elements.

    Args:
        n (int): The index of the Bell number to calculate.

    Returns:
        int: The nth Bell number.
    """
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        bell = [0] * (n + 1)
        bell[0] = 1
        bell[1] = 1
        for i in range(2, n + 1):
            for j in range(i, 0, -1):
                bell[i] += bell[j - 1]
        return bell[n]

def check(candidate):
    assert bell_Number(2) == 2
    assert bell_Number(3) == 5
    assert bell_Number(4) == 15

check(bell_Number)