def set_middle_bits(n):  
    '''
    Write a python function to toggle bits of the number except the first and the last bit. 
    Examples:
    toggle_middle_bits(9) == 15
    toggle_middle_bits(10) == 12
    toggle_middle_bits(11) == 13
    '''
def toggle_middle_bits(n):
    binary_num = bin(n)[2:]
    toggled_bits = ['0', *('1' if bit == '0' else '0' for bit in binary_num[1:-1]), '0']
    return int(''.join(toggled_bits), 2)

def check(candidate):
    assert toggle_middle_bits(9) == 15
    assert toggle_middle_bits(10) == 12
    assert toggle_middle_bits(11) == 13
    assert toggle_middle_bits(0b1000001) == 0b1111111
    assert toggle_middle_bits(0b1001101) == 0b1110011

check(set_middle_bits)