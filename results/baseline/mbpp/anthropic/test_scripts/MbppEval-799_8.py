def left_rotate(n, d):
    """
    Rotates the bits of the given number 'n' to the left by 'd' bits.
    Assumes that the number is 32 bits wide.

    Args:
        n (int): The number to be rotated.
        d (int): The number of bits to rotate.

    Returns:
        int: The number with the bits rotated to the left by 'd' bits.
    """
    # Convert the number to its binary representation
    binary = format(n, '032b')

    # Rotate the bits to the left by 'd' bits
    rotated_binary = binary[d:] + binary[:d]

    # Convert the rotated binary back to an integer and return it
    return int(rotated_binary, 2)

def check(candidate):
    assert left_rotate(16,2) == 64
    assert left_rotate(10,2) == 40
    assert left_rotate(99,3) == 792
    assert left_rotate(99,3) == 792
    assert left_rotate(0b0001,3) == 0b1000
    assert left_rotate(0b0101,3) == 0b101000
    assert left_rotate(0b11101,3) == 0b11101000

check(left_rotate)