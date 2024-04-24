def count_binary_seq(n):
    """
    Write a function to find the count of all binary sequences of length 2n such that sum of first n bits is same as sum of last n bits.

    Examples:
    count_binary_seq(1) == 2.0
    count_binary_seq(2) == 6.0
    count_binary_seq(3) == 20.0
    """
    return recursive_count(n, 0, 0, 0)

def recursive_count(n, index, first_sum, second_sum):
    """
    Recursive helper function to count the valid binary sequences.

    Args:
        n (int): The length of the binary sequence is 2n.
        index (int): The current index in the binary sequence.
        first_sum (int): The sum of the first n bits.
        second_sum (int): The sum of the last n bits.

    Returns:
        float: The count of valid binary sequences.
    """
    if index == 2 * n:
        return 1.0 if first_sum == second_sum else 0.0

    return (recursive_count(n, index + 1, first_sum + 0, second_sum + 0) +
            recursive_count(n, index + 1, first_sum + 1, second_sum + 0) +
            recursive_count(n, index + 1, first_sum + 0, second_sum + 1))

# Example usage:




def check(candidate):
    assert math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001)
    assert math.isclose(count_binary_seq(2), 6.0, rel_tol=0.001)
    assert math.isclose(count_binary_seq(3), 20.0, rel_tol=0.001)

check(count_binary_seq)