def left_rotate(n, d):
    """
    Rotate the bits of a 32-bit number `n` to the left by `d` bits.

    Args:
        n (int): The number to be rotated.
        d (int): The number of bits to rotate left.

    Returns:
        int: The rotated number.
    """
    left_shift = d % 32
    return ((n << left_shift) | (n >> (32 - left_shift))) & 0xFFFFFFFF

def check(candidate):
    assert left_rotate(16,2) == 64
    assert left_rotate(10,2) == 40
    assert left_rotate(99,3) == 792
    assert left_rotate(99,3) == 792
    assert left_rotate(0b0001,3) == 0b1000
    assert left_rotate(0b0101,3) == 0b101000
    assert left_rotate(0b11101,3) == 0b11101000

check(left_rotate)