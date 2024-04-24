def left_rotate(n, d):
    """
    Rotates the bits of the given number 'n' to the left by 'd' bits.
    We assume that the number is 32 bit.
    """
    # Ensure d is within the range of 32 bits
    d = d % 32

    # Shift the bits to the left by d bits
    left_shifted = (n << d) & 0xFFFFFFFF

    # Shift the bits to the right by (32 - d) bits
    right_shifted = (n >> (32 - d)) & 0xFFFFFFFF

    # Combine the left and right shifted bits
    rotated = left_shifted | right_shifted

    return rotated

def check(candidate):
    assert left_rotate(16,2) == 64
    assert left_rotate(10,2) == 40
    assert left_rotate(99,3) == 792
    assert left_rotate(99,3) == 792
    assert left_rotate(0b0001,3) == 0b1000
    assert left_rotate(0b0101,3) == 0b101000
    assert left_rotate(0b11101,3) == 0b11101000

check(left_rotate)