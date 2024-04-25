def set_left_most_unset_bit(n):
    binary_str = bin(n)[2:]
    unset_bit_position = binary_str.find('0')
    result = n | (1 << (len(binary_str) - unset_bit_position - 1))
    return result

def check(candidate):
    assert set_left_most_unset_bit(10) == 14
    assert set_left_most_unset_bit(12) == 14
    assert set_left_most_unset_bit(15) == 15

check(set_left_most_unset_bit)