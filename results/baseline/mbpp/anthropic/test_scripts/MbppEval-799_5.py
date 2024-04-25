def left_rotate(n, d):
    """
    Rotates the bits of the given 32-bit number n to the left by d bits.
    
    Args:
        n (int): The number to be rotated.
        d (int): The number of bits to rotate.
        
    Returns:
        int: The number with its bits rotated to the left by d bits.
    """
    # Convert the number to binary string and pad it with leading zeros to 32 bits
    bin_str = "{0:032b}".format(n)
    
    # Rotate the bits to the left by d bits
    rotated_bin_str = bin_str[d:] + bin_str[:d]
    
    # Convert the rotated binary string back to an integer
    return int(rotated_bin_str, 2)

def check(candidate):
    assert left_rotate(16,2) == 64
    assert left_rotate(10,2) == 40
    assert left_rotate(99,3) == 792
    assert left_rotate(99,3) == 792
    assert left_rotate(0b0001,3) == 0b1000
    assert left_rotate(0b0101,3) == 0b101000
    assert left_rotate(0b11101,3) == 0b11101000

check(left_rotate)