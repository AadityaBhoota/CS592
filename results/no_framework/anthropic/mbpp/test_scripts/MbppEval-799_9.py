def left_rotate(n, d):
    """
    Rotates the bits of a 32-bit integer `n` to the left by `d` bits.

    Args:
        n (int): The 32-bit integer to be rotated.
        d (int): The number of bits to rotate.

    Returns:
        int: The result of rotating the bits of `n` to the left by `d` bits.
    """
    # Ensure that the number of bits to rotate is within the valid range (0 to 31)
    d = d % 32

    # Shift the bits to the left by `d` bits
    left_shifted = n << d

    # Shift the bits to the right by (32 - d) bits to get the rotated result
    right_shifted = n >> (32 - d)

    # Combine the left-shifted and right-shifted bits to get the final result
    return (left_shifted | right_shifted)

def check(candidate):
    assert left_rotate(16,2) == 64
    assert left_rotate(10,2) == 40
    assert left_rotate(99,3) == 792
    assert left_rotate(99,3) == 792
    assert left_rotate(0b0001,3) == 0b1000
    assert left_rotate(0b0101,3) == 0b101000
    assert left_rotate(0b11101,3) == 0b11101000

check(left_rotate)