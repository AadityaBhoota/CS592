def set_left_most_unset_bit(n):
    """
    Write a python function to set the left most unset bit.

    Examples:
    set_left_most_unset_bit(10) == 14
    set_left_most_unset_bit(12) == 14
    set_left_most_unset_bit(15) == 15
    """
    # Convert the number to binary string
    binary = bin(n)[2:]

    # Find the index of the leftmost unset bit
    leftmost_unset_idx = next((i for i, bit in enumerate(reversed(binary)) if bit == '0'), -1)

    # If there is no unset bit, return the original number
    if leftmost_unset_idx == -1:
        return n

    # Set the leftmost unset bit
    return n | (1 << (len(binary) - leftmost_unset_idx - 1))

def check(candidate):
    assert set_left_most_unset_bit(10) == 14
    assert set_left_most_unset_bit(12) == 14
    assert set_left_most_unset_bit(15) == 15

check(set_left_most_unset_bit)