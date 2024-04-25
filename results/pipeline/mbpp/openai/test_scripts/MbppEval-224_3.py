def count_Set_Bits(n):
    count = 0

    while n > 0:
        if n & 1:
            count += 1
        
        n = n >> 1

    return count

def check(candidate):
    assert count_Set_Bits(2) == 1
    assert count_Set_Bits(4) == 1
    assert count_Set_Bits(6) == 2

check(count_Set_Bits)