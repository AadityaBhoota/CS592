def left_rotate(n, d):
    # number of bits in a 32-bit integer
    num_bits = 32

    # mask for clearing the bits to be shifted
    mask = (1 << num_bits) - 1

    # extract the bits that will be shifted out
    shifted_bits = (n >> (num_bits - d)) & ((1 << d) - 1)

    # shift the number to the left by d bits
    result = ((n << d) | shifted_bits) & mask

    return result

# Test cases




def check(candidate):
    assert left_rotate(16,2) == 64
    assert left_rotate(10,2) == 40
    assert left_rotate(99,3) == 792
    assert left_rotate(99,3) == 792
    assert left_rotate(0b0001,3) == 0b1000
    assert left_rotate(0b0101,3) == 0b101000
    assert left_rotate(0b11101,3) == 0b11101000

check(left_rotate)