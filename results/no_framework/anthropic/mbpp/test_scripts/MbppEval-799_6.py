def left_rotate(n, d):
    """
    Rotate the bits of the given number 'n' to the left by 'd' bits.
    We assume that the number is 32 bits.
    
    Examples:
    left_rotate(16, 2) == 64
    left_rotate(10, 2) == 40
    left_rotate(99, 3) == 792
    """
    # Convert the number to binary string
    binary_str = bin(n)[2:].zfill(32)
    
    # Perform the left rotation
    rotated_binary = binary_str[d:] + binary_str[:d]
    
    # Convert the rotated binary string back to an integer
    rotated_number = int(rotated_binary, 2)
    
    return rotated_number

def check(candidate):
    assert left_rotate(16,2) == 64
    assert left_rotate(10,2) == 40
    assert left_rotate(99,3) == 792
    assert left_rotate(99,3) == 792
    assert left_rotate(0b0001,3) == 0b1000
    assert left_rotate(0b0101,3) == 0b101000
    assert left_rotate(0b11101,3) == 0b11101000

check(left_rotate)