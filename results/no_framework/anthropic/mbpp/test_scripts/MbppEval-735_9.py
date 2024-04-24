def set_middle_bits(n):
    """
    Write a Python function to toggle bits of the number except the first and the last bit.
    Examples:
    toggle_middle_bits(9) == 15
    toggle_middle_bits(10) == 12
    toggle_middle_bits(11) == 13
    """
    binary_str = bin(n)[2:]  # convert the number to binary string and remove the "0b" prefix
    middle_bits = binary_str[1:-1]  # get the middle bits
    
    # Toggle the middle bits
    toggled_middle_bits = ''.join('1' if bit == '0' else '0' for bit in middle_bits)
    
    # Reconstruct the binary string with the toggled middle bits
    result = binary_str[0] + toggled_middle_bits + binary_str[-1]
    
    return int(result, 2)  # convert the binary string back to decimal

def check(candidate):
    assert toggle_middle_bits(9) == 15
    assert toggle_middle_bits(10) == 12
    assert toggle_middle_bits(11) == 13
    assert toggle_middle_bits(0b1000001) == 0b1111111
    assert toggle_middle_bits(0b1001101) == 0b1110011

check(set_middle_bits)