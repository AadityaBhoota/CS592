def set_middle_bits(n):
    binary_num = bin(n)[2:]
    toggled_num = '1' + ''.join('0' if bit == '1' else '1' for bit in binary_num[1:-1]) + '1'
    return int(toggled_num, 2)

def check(candidate):
    assert toggle_middle_bits(9) == 15
    assert toggle_middle_bits(10) == 12
    assert toggle_middle_bits(11) == 13
    assert toggle_middle_bits(0b1000001) == 0b1111111
    assert toggle_middle_bits(0b1001101) == 0b1110011

check(set_middle_bits)