def left_rotate(n, d):
    """
    Write a function that rotates the bits of a given number n to the left by d bits.
    We assume that the number is 32 bit.

    Examples:
    left_rotate(16, 2) == 64
    left_rotate(10, 2) == 40
    left_rotate(99, 3) == 792
    """
    # Ensure that the rotation amount is within the range of 32 bits
    d %= 32

    # Perform the left rotation using bitwise operations
    return ((n << d) | (n >> (32 - d))) & 0xFFFFFFFF

def check(candidate):
    assert left_rotate(16,2) == 64
    assert left_rotate(10,2) == 40
    assert left_rotate(99,3) == 792
    assert left_rotate(99,3) == 792
    assert left_rotate(0b0001,3) == 0b1000
    assert left_rotate(0b0101,3) == 0b101000
    assert left_rotate(0b11101,3) == 0b11101000

check(left_rotate)