def count_binary_seq(n):
    """
    Write a function to find the count of all binary sequences of length 2n such that sum of first n bits is same as sum of last n bits.

    Examples:
    count_binary_seq(1) == 2.0
    count_binary_seq(2) == 6.0
    count_binary_seq(3) == 20.0
    """
    # Base case: for n = 1, there are 2 valid sequences (01, 10)
    if n == 1:
        return 2.0

    # Recursive case: for n > 1, we can use the formula:
    # count(n) = 2 * count(n-1) + 2^(n-1)
    return 2 * count_binary_seq(n - 1) + 2 ** (n - 1)

def check(candidate):
    assert math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001)
    assert math.isclose(count_binary_seq(2), 6.0, rel_tol=0.001)
    assert math.isclose(count_binary_seq(3), 20.0, rel_tol=0.001)

check(count_binary_seq)