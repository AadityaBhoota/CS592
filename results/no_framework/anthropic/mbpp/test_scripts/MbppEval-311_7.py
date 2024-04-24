def set_left_most_unset_bit(n):
    """
    Write a python function to set the left most unset bit.

    Examples:
    set_left_most_unset_bit(10) == 14
    set_left_most_unset_bit(12) == 14
    set_left_most_unset_bit(15) == 15
    """
    # Convert the number to binary string
    bin_str = bin(n)[2:]

    # Find the index of the leftmost unset bit
    leftmost_unset_index = next((i for i, bit in enumerate(reversed(bin_str)) if bit == '0'), None)

    # If all bits are set, return the original number
    if leftmost_unset_index is None:
        return n

    # Set the leftmost unset bit
    set_bit_mask = 2 ** (len(bin_str) - leftmost_unset_index - 1)
    return n | set_bit_mask

def check(candidate):
    assert set_left_most_unset_bit(10) == 14
    assert set_left_most_unset_bit(12) == 14
    assert set_left_most_unset_bit(15) == 15

check(set_left_most_unset_bit)