def set_left_most_unset_bit(n): 
    # Find the position of the left most unset bit
    pos = 0
    while ((n >> pos) & 1):
        pos += 1
    
    # Set the left most unset bit
    return n | (1 << pos)

# Test cases




def check(candidate):
    assert set_left_most_unset_bit(10) == 14
    assert set_left_most_unset_bit(12) == 14
    assert set_left_most_unset_bit(15) == 15

check(set_left_most_unset_bit)