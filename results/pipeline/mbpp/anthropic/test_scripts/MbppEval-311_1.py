def set_left_most_unset_bit(n):
    binary_str = bin(n)[2:]
    leftmost_unset_bit_pos = 0
    for i, bit in enumerate(binary_str):
        if bit == '0':
            leftmost_unset_bit_pos = len(binary_str) - i
            break
    result = n | (1 << (leftmost_unset_bit_pos - 1))
    return result

def check(candidate):
    assert set_left_most_unset_bit(10) == 14
    assert set_left_most_unset_bit(12) == 14
    assert set_left_most_unset_bit(15) == 15

check(set_left_most_unset_bit)