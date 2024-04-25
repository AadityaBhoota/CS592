def set_left_most_unset_bit(n):
    position = 0
    while n & (1 << position):
        position += 1
    return n | (1 << position)

def check(candidate):
    assert set_left_most_unset_bit(10) == 14
    assert set_left_most_unset_bit(12) == 14
    assert set_left_most_unset_bit(15) == 15

check(set_left_most_unset_bit)