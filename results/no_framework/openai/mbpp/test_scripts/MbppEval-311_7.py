
def set_left_most_unset_bit(n):
    if n == 0:
        return 1
    num_bits = n.bit_length()
    max_num = 1 << (num_bits + 1)
    return n | (max_num - 1)


# Test cases





def check(candidate):
    assert set_left_most_unset_bit(10) == 14
    assert set_left_most_unset_bit(12) == 14
    assert set_left_most_unset_bit(15) == 15

check(set_left_most_unset_bit)