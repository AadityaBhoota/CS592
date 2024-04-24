def count_binary_seq(n):
    """
    Find the count of all binary sequences of length 2n such that sum of first n bits is same as sum of last n bits.
    """
    total_count = 0
    for num in range(2 ** (2 * n)):
        binary_seq = format(num, f'0{2 * n}b')
        first_half = int(binary_seq[:n], 2)
        second_half = int(binary_seq[n:], 2)
        if first_half == second_half:
            total_count += 1
    return total_count

def check(candidate):
    assert math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001)
    assert math.isclose(count_binary_seq(2), 6.0, rel_tol=0.001)
    assert math.isclose(count_binary_seq(3), 20.0, rel_tol=0.001)

check(count_binary_seq)