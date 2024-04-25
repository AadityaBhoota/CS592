def set_middle_bits(n):
    binary_str = bin(n)[2:]
    middle_bits = binary_str[1:-1]
    toggled_middle_bits = ''.join('1' if bit == '0' else '0' for bit in middle_bits)
    new_binary_str = binary_str[0] + toggled_middle_bits + binary_str[-1]
    return int(new_binary_str, 2)

def check(candidate):
    assert toggle_middle_bits(9) == 15
    assert toggle_middle_bits(10) == 12
    assert toggle_middle_bits(11) == 13
    assert toggle_middle_bits(0b1000001) == 0b1111111
    assert toggle_middle_bits(0b1001101) == 0b1110011

check(set_middle_bits)