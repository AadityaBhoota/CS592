def count_binary_seq(n):
    """
    Write a function to find the count of all binary sequences of length 2n such that sum of first n bits is same as sum of last n bits.

    Examples:
    count_binary_seq(1) == 2.0
    count_binary_seq(2) == 6.0
    count_binary_seq(3) == 20.0
    """
    if n == 1:
        return 2.0

    count = 0
    for i in range(2 ** (2 * n)):
        binary_seq = format(i, f"0{2 * n}b")
        first_half = int(binary_seq[:n], 2)
        second_half = int(binary_seq[n:], 2)
        if first_half == second_half:
            count += 1

    return count

def check(candidate):
    assert math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001)
    assert math.isclose(count_binary_seq(2), 6.0, rel_tol=0.001)
    assert math.isclose(count_binary_seq(3), 20.0, rel_tol=0.001)

check(count_binary_seq)