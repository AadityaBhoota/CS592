def pair_xor_Sum(arr, n):
    xor_sum = 0
    
    for i in range(n):
        for j in range(i+1, n):
            xor_sum += arr[i] ^ arr[j]
    
    return xor_sum

# Test the function with the examples provided




def check(candidate):
    assert pair_xor_Sum([5,9,7,6],4) == 47
    assert pair_xor_Sum([7,3,5],3) == 12
    assert pair_xor_Sum([7,3],2) == 4

check(pair_xor_Sum)