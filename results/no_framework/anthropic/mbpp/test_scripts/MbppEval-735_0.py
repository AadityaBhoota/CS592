def set_middle_bits(n):
    """
    Write a Python function to toggle bits of the number except the first and the last bit.

    Examples:
    set_middle_bits(9) == 15
    set_middle_bits(10) == 12
    set_middle_bits(11) == 13
    """
    binary_str = bin(n)[2:] # Convert the number to binary string, and remove the '0b' prefix
    result = int(binary_str[0] + ''.join(['1' if bit == '0' else '0' for bit in binary_str[1:-1]]) + binary_str[-1], 2)
    return result

def check(candidate):
    assert toggle_middle_bits(9) == 15
    assert toggle_middle_bits(10) == 12
    assert toggle_middle_bits(11) == 13
    assert toggle_middle_bits(0b1000001) == 0b1111111
    assert toggle_middle_bits(0b1001101) == 0b1110011

check(set_middle_bits)