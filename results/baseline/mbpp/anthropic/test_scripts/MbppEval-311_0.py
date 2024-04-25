def set_left_most_unset_bit(n):
    """
    Write a python function to set the left most unset bit.

    Examples:
    set_left_most_unset_bit(10) == 14
    set_left_most_unset_bit(12) == 14
    set_left_most_unset_bit(15) == 15
    """
    if n == 0:
        return 1
    
    # Find the leftmost set bit
    leftmost_set_bit = 1
    while n & leftmost_set_bit == 0:
        leftmost_set_bit <<= 1
    
    # Shift the leftmost set bit one position to the left
    return n | (leftmost_set_bit << 1)

def check(candidate):
    assert set_left_most_unset_bit(10) == 14
    assert set_left_most_unset_bit(12) == 14
    assert set_left_most_unset_bit(15) == 15

check(set_left_most_unset_bit)