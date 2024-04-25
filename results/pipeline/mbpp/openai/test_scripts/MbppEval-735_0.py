def set_middle_bits(n):
    mask = 0
    num_bits = n.bit_length()
    mask = (1 << (num_bits - 1)) | 1
    
    result = n ^ mask
    return result

def check(candidate):
    assert toggle_middle_bits(9) == 15
    assert toggle_middle_bits(10) == 12
    assert toggle_middle_bits(11) == 13
    assert toggle_middle_bits(0b1000001) == 0b1111111
    assert toggle_middle_bits(0b1001101) == 0b1110011

check(set_middle_bits)