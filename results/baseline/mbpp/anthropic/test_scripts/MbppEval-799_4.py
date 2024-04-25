def left_rotate(n, d):
    """
    Rotate the bits of a given 32-bit number n to the left by d bits.

    Args:
    n (int): The 32-bit number to be rotated.
    d (int): The number of bits to rotate.

    Returns:
    int: The result of rotating the bits of n to the left by d bits.
    """
    # Ensure that d is within the range of 32 bits
    d = d % 32

    # Rotate the bits to the left by d bits
    return (n << d) | (n >> (32 - d))

def check(candidate):
    assert left_rotate(16,2) == 64
    assert left_rotate(10,2) == 40
    assert left_rotate(99,3) == 792
    assert left_rotate(99,3) == 792
    assert left_rotate(0b0001,3) == 0b1000
    assert left_rotate(0b0101,3) == 0b101000
    assert left_rotate(0b11101,3) == 0b11101000

check(left_rotate)