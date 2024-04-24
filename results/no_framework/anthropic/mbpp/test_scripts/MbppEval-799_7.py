def left_rotate(n, d):
    """
    Rotates the bits of a 32-bit number n to the left by d bits.

    Args:
        n (int): The number to be rotated.
        d (int): The number of bits to rotate.

    Returns:
        int: The rotated number.
    """
    # Convert the number to a binary string
    binary = format(n, '032b')

    # Perform the left rotation
    rotated_binary = binary[d:] + binary[:d]

    # Convert the rotated binary string back to an integer
    rotated_n = int(rotated_binary, 2)

    return rotated_n

def check(candidate):
    assert left_rotate(16,2) == 64
    assert left_rotate(10,2) == 40
    assert left_rotate(99,3) == 792
    assert left_rotate(99,3) == 792
    assert left_rotate(0b0001,3) == 0b1000
    assert left_rotate(0b0101,3) == 0b101000
    assert left_rotate(0b11101,3) == 0b11101000

check(left_rotate)