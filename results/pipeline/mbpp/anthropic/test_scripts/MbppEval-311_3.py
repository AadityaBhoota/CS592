def set_left_most_unset_bit(n):
    leftmost_one = n & (-n)
    return n | leftmost_one

def check(candidate):
    assert set_left_most_unset_bit(10) == 14
    assert set_left_most_unset_bit(12) == 14
    assert set_left_most_unset_bit(15) == 15

check(set_left_most_unset_bit)