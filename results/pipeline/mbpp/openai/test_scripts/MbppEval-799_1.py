def left_rotate(n, d):
    bin_str = bin(n)[2:].zfill(32)
    rotated_bin_str = bin_str[d:] + bin_str[:d]
    rotated_num = int(rotated_bin_str, 2)
    
    return rotated_num

def check(candidate):
    assert left_rotate(16,2) == 64
    assert left_rotate(10,2) == 40
    assert left_rotate(99,3) == 792
    assert left_rotate(99,3) == 792
    assert left_rotate(0b0001,3) == 0b1000
    assert left_rotate(0b0101,3) == 0b101000
    assert left_rotate(0b11101,3) == 0b11101000

check(left_rotate)