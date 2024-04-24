def left_rotate(n, d):
    # Ensure d is within range 0 to 31
    actual_rotation = d % 32

    # Perform left rotation by shifting bits to the left and adding bits shifted out back to the right
    result = (n << actual_rotation) | (n >> (32 - actual_rotation))

    return result

# Test the function




def check(candidate):
    assert left_rotate(16,2) == 64
    assert left_rotate(10,2) == 40
    assert left_rotate(99,3) == 792
    assert left_rotate(99,3) == 792
    assert left_rotate(0b0001,3) == 0b1000
    assert left_rotate(0b0101,3) == 0b101000
    assert left_rotate(0b11101,3) == 0b11101000

check(left_rotate)