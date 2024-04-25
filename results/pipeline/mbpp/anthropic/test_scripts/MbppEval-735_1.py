def set_middle_bits(n):
    if n in (0, 1):
        return n
    num_bits = len(bin(n)) - 2
    mask = (1 << num_bits) - 2
    return n ^ mask

def check(candidate):
    assert toggle_middle_bits(9) == 15
    assert toggle_middle_bits(10) == 12
    assert toggle_middle_bits(11) == 13
    assert toggle_middle_bits(0b1000001) == 0b1111111
    assert toggle_middle_bits(0b1001101) == 0b1110011

check(set_middle_bits)