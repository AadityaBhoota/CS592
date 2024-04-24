def set_middle_bits(n):
    """
    Write a python function to toggle bits of the number except the first and the last bit.
    Examples:
    set_middle_bits(9) == 15
    set_middle_bits(10) == 12
    set_middle_bits(11) == 13
    """
    # Convert the number to binary string
    binary_str = bin(n)[2:]
    
    # Flip the middle bits
    result = ""
    for i in range(1, len(binary_str) - 1):
        if binary_str[i] == "0":
            result += "1"
        else:
            result += "0"
    
    # Append the first and last bits
    result = binary_str[0] + result + binary_str[-1]
    
    # Convert the result back to decimal
    return int(result, 2)

def check(candidate):
    assert toggle_middle_bits(9) == 15
    assert toggle_middle_bits(10) == 12
    assert toggle_middle_bits(11) == 13
    assert toggle_middle_bits(0b1000001) == 0b1111111
    assert toggle_middle_bits(0b1001101) == 0b1110011

check(set_middle_bits)