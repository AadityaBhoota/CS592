def odd_num_sum(n):
    """
    Find the sum of the fourth power of the first n odd natural numbers.

    Args:
    n (int): The number of odd natural numbers to consider.

    Returns:
    int: The sum of the fourth power of the first n odd natural numbers.
    """
    return sum([(2 * i - 1) ** 4 for i in range(1, n + 1)])

def check(candidate):
    assert odd_num_sum(2) == 82
    assert odd_num_sum(3) == 707
    assert odd_num_sum(4) == 3108

check(odd_num_sum)