def set_middle_bits(n):
    binary_str = bin(n)[2:]  # Convert the given number into a binary string
    
    first_bit = binary_str[0]
    last_bit = binary_str[-1]
    
    middle_bits = ''.join(['0' if bit == '1' else '1' for bit in binary_str[1:-1]])  # Toggle the middle bits
    
    return int(first_bit + middle_bits + last_bit, 2)  # Convert binary back to integer

def check(candidate):
    assert toggle_middle_bits(9) == 15
    assert toggle_middle_bits(10) == 12
    assert toggle_middle_bits(11) == 13
    assert toggle_middle_bits(0b1000001) == 0b1111111
    assert toggle_middle_bits(0b1001101) == 0b1110011

check(set_middle_bits)