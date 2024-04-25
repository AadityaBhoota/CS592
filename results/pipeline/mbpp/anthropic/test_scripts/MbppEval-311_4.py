def set_left_most_unset_bit(n):
    position = n.bit_length()
    mask = (1 << position) - 1
    return n | mask

def check(candidate):
    assert set_left_most_unset_bit(10) == 14
    assert set_left_most_unset_bit(12) == 14
    assert set_left_most_unset_bit(15) == 15

check(set_left_most_unset_bit)