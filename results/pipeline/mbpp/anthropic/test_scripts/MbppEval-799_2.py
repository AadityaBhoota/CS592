def left_rotate(n, d):
    bin_n = format(n, '032b')
    rotated_bits = bin_n[d:] + bin_n[:d]
    return int(rotated_bits, 2)

def check(candidate):
    assert left_rotate(16,2) == 64
    assert left_rotate(10,2) == 40
    assert left_rotate(99,3) == 792
    assert left_rotate(99,3) == 792
    assert left_rotate(0b0001,3) == 0b1000
    assert left_rotate(0b0101,3) == 0b101000
    assert left_rotate(0b11101,3) == 0b11101000

check(left_rotate)