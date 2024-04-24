def set_left_most_unset_bit(n):
    if n == 0:
        return 1
    unset_bit = (~n) & (n + 1)
    return n | unset_bit

# Test cases




def check(candidate):
    assert set_left_most_unset_bit(10) == 14
    assert set_left_most_unset_bit(12) == 14
    assert set_left_most_unset_bit(15) == 15

check(set_left_most_unset_bit)