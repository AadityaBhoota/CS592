def count_binary_seq(n):
    """
    Write a function to find the count of all binary sequences of length 2n such that the sum of the first n bits is the same as the sum of the last n bits.
    """
    # Initialize the count to 0
    count = 0

    # Generate all possible binary sequences of length 2n
    for i in range(2 ** (2 * n)):
        # Convert the current integer to a binary string of length 2n
        binary_seq = format(i, f'0{2 * n}b')

        # Check if the sum of the first n bits is the same as the sum of the last n bits
        first_half = sum(int(bit) for bit in binary_seq[:n])
        second_half = sum(int(bit) for bit in binary_seq[n:])
        if first_half == second_half:
            count += 1

    return count

def check(candidate):
    assert math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001)
    assert math.isclose(count_binary_seq(2), 6.0, rel_tol=0.001)
    assert math.isclose(count_binary_seq(3), 20.0, rel_tol=0.001)

check(count_binary_seq)