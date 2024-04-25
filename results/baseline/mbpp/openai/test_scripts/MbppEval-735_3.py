def set_middle_bits(n):  
    '''
    Write a python function to toggle bits of the number except the first and the last bit. 
    Examples:
    toggle_middle_bits(9) == 15
    toggle_middle_bits(10) == 12
    toggle_middle_bits(11) == 13
    '''
def toggle_middle_bits(n):  
    mask = (1 << n.bit_length()) - 3
    return n ^ mask

# Test cases




def check(candidate):
    assert toggle_middle_bits(9) == 15
    assert toggle_middle_bits(10) == 12
    assert toggle_middle_bits(11) == 13
    assert toggle_middle_bits(0b1000001) == 0b1111111
    assert toggle_middle_bits(0b1001101) == 0b1110011

check(set_middle_bits)