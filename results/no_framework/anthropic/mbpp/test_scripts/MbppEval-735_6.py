def set_middle_bits(n):
    """
    Write a python function to toggle bits of the number except the first and the last bit.
    Examples:
    toggle_middle_bits(9) == 15
    toggle_middle_bits(10) == 12
    toggle_middle_bits(11) == 13
    """
    # Convert the number to binary string
    binary_str = bin(n)[2:]
    
    # Toggle the middle bits
    middle_bits = "".join("1" if bit == "0" else "0" for bit in binary_str[1:-1])
    
    # Reconstruct the binary string with the toggled middle bits
    result = binary_str[0] + middle_bits + binary_str[-1]
    
    # Convert the binary string back to integer
    return int(result, 2)

def check(candidate):
    assert toggle_middle_bits(9) == 15
    assert toggle_middle_bits(10) == 12
    assert toggle_middle_bits(11) == 13
    assert toggle_middle_bits(0b1000001) == 0b1111111
    assert toggle_middle_bits(0b1001101) == 0b1110011

check(set_middle_bits)