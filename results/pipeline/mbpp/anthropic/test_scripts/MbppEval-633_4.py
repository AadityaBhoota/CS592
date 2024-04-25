def pair_xor_Sum(arr, n):
    total_xor_sum = 0
    
    # Step 2: Calculate the XOR of all elements
    for num in arr:
        total_xor_sum ^= num
    
    # Step 3: XOR each element with the total XOR
    for num in arr:
        total_xor_sum ^= num
    
    return total_xor_sum

def check(candidate):
    assert pair_xor_Sum([5,9,7,6],4) == 47
    assert pair_xor_Sum([7,3,5],3) == 12
    assert pair_xor_Sum([7,3],2) == 4

check(pair_xor_Sum)