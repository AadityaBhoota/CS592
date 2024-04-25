def set_left_most_unset_bit(n):
    """
    Set the leftmost unset bit in the given integer n.
    """
    # Find the rightmost set bit
    rightmost_set_bit = n & -n
    
    # Shift the rightmost set bit all the way to the left
    leftmost_unset_bit = rightmost_set_bit << 1
    
    # Set the leftmost unset bit
    return n | leftmost_unset_bit

def check(candidate):
    assert set_left_most_unset_bit(10) == 14
    assert set_left_most_unset_bit(12) == 14
    assert set_left_most_unset_bit(15) == 15

check(set_left_most_unset_bit)