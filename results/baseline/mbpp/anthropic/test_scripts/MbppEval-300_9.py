def count_binary_seq(n):
    """
    Write a function to find the count of all binary sequences of length 2n such that sum of first n bits is same as sum of last n bits.

    Examples:
    count_binary_seq(1) == 2.0
    count_binary_seq(2) == 6.0
    count_binary_seq(3) == 20.0
    """
    if n == 0:
        return 0.0

    # Total number of binary sequences of length 2n
    total_sequences = 2 ** (2 * n)

    # Initialize the count of valid sequences
    valid_sequences = 0

    # Iterate through all possible binary sequences
    for i in range(total_sequences):
        # Convert the current integer to a binary string of length 2n
        binary_seq = format(i, f'0{2 * n}b')

        # Split the binary sequence into the first n bits and the last n bits
        first_n_bits = int(binary_seq[:n], 2)
        last_n_bits = int(binary_seq[n:], 2)

        # Check if the sum of the first n bits is equal to the sum of the last n bits
        if first_n_bits == last_n_bits:
            valid_sequences += 1

    return valid_sequences

def check(candidate):
    assert math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001)
    assert math.isclose(count_binary_seq(2), 6.0, rel_tol=0.001)
    assert math.isclose(count_binary_seq(3), 20.0, rel_tol=0.001)

check(count_binary_seq)