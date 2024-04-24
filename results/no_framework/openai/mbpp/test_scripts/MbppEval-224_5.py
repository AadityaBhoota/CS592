def count_Set_Bits(n): 
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

# Testing the function with the given examples
assert count_Set_Bits(2) == 1
assert count_Set_Bits(4) == 1
assert count_Set_Bits(6) == 2

def check(candidate):
    assert count_Set_Bits(2) == 1
    assert count_Set_Bits(4) == 1
    assert count_Set_Bits(6) == 2

check(count_Set_Bits)