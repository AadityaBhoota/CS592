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
    
    # Find the left-most set bit
    x = 1
    while x <= n:
        x <<= 1
    
    # Set the left-most unset bit
    return n | (x >> 1)

def check(candidate):
    assert set_left_most_unset_bit(10) == 14
    assert set_left_most_unset_bit(12) == 14
    assert set_left_most_unset_bit(15) == 15

check(set_left_most_unset_bit)