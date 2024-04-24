def count_Set_Bits(n): 
    # Using bitwise manipulation to count set bits
    count = 0
    while n: 
        count += n & 1
        n >>= 1
    return count

# Test cases




def check(candidate):
    assert count_Set_Bits(2) == 1
    assert count_Set_Bits(4) == 1
    assert count_Set_Bits(6) == 2

check(count_Set_Bits)