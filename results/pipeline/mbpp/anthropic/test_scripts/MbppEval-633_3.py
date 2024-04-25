def pair_xor_Sum(arr, n):
    total_xor_sum = 0
    for a in arr:
        total_xor_sum ^= a
    
    result = 0
    for a in arr:
        result += total_xor_sum ^ a
    
    return result

def check(candidate):
    assert pair_xor_Sum([5,9,7,6],4) == 47
    assert pair_xor_Sum([7,3,5],3) == 12
    assert pair_xor_Sum([7,3],2) == 4

check(pair_xor_Sum)