def set_middle_bits(n):
    """
    Write a Python function to toggle bits of the number except the first and the last bit.
    
    Examples:
    set_middle_bits(9) == 15
    set_middle_bits(10) == 12
    set_middle_bits(11) == 13
    """
    # Convert the number to binary string
    binary_str = bin(n)[2:]
    
    # Flip the middle bits (excluding the first and last bits)
    middle_bits = binary_str[1:-1]
    middle_bits = ''.join(['0' if bit == '1' else '1' for bit in middle_bits])
    
    # Reconstruct the binary string with the modified middle bits
    new_binary_str = binary_str[0] + middle_bits + binary_str[-1]
    
    # Convert the modified binary string back to a number and return it
    return int(new_binary_str, 2)

def check(candidate):
    assert toggle_middle_bits(9) == 15
    assert toggle_middle_bits(10) == 12
    assert toggle_middle_bits(11) == 13
    assert toggle_middle_bits(0b1000001) == 0b1111111
    assert toggle_middle_bits(0b1001101) == 0b1110011

check(set_middle_bits)