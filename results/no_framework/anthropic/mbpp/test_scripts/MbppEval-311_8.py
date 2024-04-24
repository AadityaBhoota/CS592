def set_left_most_unset_bit(n):
    """
    Write a python function to set the left most unset bit.

    Examples:
    set_left_most_unset_bit(10) == 14
    set_left_most_unset_bit(12) == 14
    set_left_most_unset_bit(15) == 15
    """
    # Convert the number to binary string
    binary_str = bin(n)[2:]

    # Find the index of the leftmost '0' (unset bit)
    leftmost_unset_index = next((i for i, bit in enumerate(binary_str[::-1]) if bit == '0'), None)

    if leftmost_unset_index is None:
        # If all bits are set, return the original number
        return n
    else:
        # Set the leftmost unset bit to 1
        return n | (1 << (len(binary_str) - leftmost_unset_index - 1))

def check(candidate):
    assert set_left_most_unset_bit(10) == 14
    assert set_left_most_unset_bit(12) == 14
    assert set_left_most_unset_bit(15) == 15

check(set_left_most_unset_bit)