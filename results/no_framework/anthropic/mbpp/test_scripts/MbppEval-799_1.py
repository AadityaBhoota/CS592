def left_rotate(n, d):
    """
    Write a function to that rotate left bits by d bits a given number. We assume that the number is 32 bit.

    Examples:
    left_Rotate(16, 2) == 64
    left_Rotate(10, 2) == 40
    left_Rotate(99, 3) == 792
    """
    # Convert the number to its binary representation
    binary = format(n, '032b')

    # Perform the left rotation
    rotated_binary = binary[d:] + binary[:d]

    # Convert the rotated binary back to an integer
    rotated_number = int(rotated_binary, 2)

    return rotated_number

def check(candidate):
    assert left_rotate(16,2) == 64
    assert left_rotate(10,2) == 40
    assert left_rotate(99,3) == 792
    assert left_rotate(99,3) == 792
    assert left_rotate(0b0001,3) == 0b1000
    assert left_rotate(0b0101,3) == 0b101000
    assert left_rotate(0b11101,3) == 0b11101000

check(left_rotate)