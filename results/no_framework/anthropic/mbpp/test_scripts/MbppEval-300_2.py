def count_binary_seq(n):
    """
    Find the count of all binary sequences of length 2n such that the sum of the first n bits is
    the same as the sum of the last n bits.

    Args:
        n (int): The length of the binary sequence.

    Returns:
        float: The count of all binary sequences that satisfy the given condition.
    """
    # Initialize the count to 0
    count = 0

    # Iterate over all possible binary sequences of length 2n
    for i in range(2 ** (2 * n)):
        # Convert the current integer to a binary string of length 2n
        binary_str = bin(i)[2:].zfill(2 * n)

        # Check if the sum of the first n bits is the same as the sum of the last n bits
        if sum(map(int, binary_str[:n])) == sum(map(int, binary_str[n:])):
            count += 1

    return count

# Test the function




def check(candidate):
    assert math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001)
    assert math.isclose(count_binary_seq(2), 6.0, rel_tol=0.001)
    assert math.isclose(count_binary_seq(3), 20.0, rel_tol=0.001)

check(count_binary_seq)