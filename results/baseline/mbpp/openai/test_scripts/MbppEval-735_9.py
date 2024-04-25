def set_middle_bits(n):  
    '''
    Write a python function to toggle bits of the number except the first and the last bit. 
    Examples:
    toggle_middle_bits(9) == 15
    toggle_middle_bits(10) == 12
    toggle_middle_bits(11) == 13
    '''
def toggle_middle_bits(n):
    # Find the total number of bits
    num_bits = n.bit_length()

    # Generate a mask to toggle all middle bits
    mask = 2 ** (num_bits - 2) - 1

    # Toggle all middle bits using XOR with the mask
    result = n ^ mask

    return result

# Test the function with the given examples




def check(candidate):
    assert toggle_middle_bits(9) == 15
    assert toggle_middle_bits(10) == 12
    assert toggle_middle_bits(11) == 13
    assert toggle_middle_bits(0b1000001) == 0b1111111
    assert toggle_middle_bits(0b1001101) == 0b1110011

check(set_middle_bits)