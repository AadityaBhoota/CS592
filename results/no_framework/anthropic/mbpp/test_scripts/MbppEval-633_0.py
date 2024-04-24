def pair_xor_Sum(arr, n):
    total_xor = 0
    for i in range(n):
        for j in range(i+1, n):
            total_xor += arr[i] ^ arr[j]
    return total_xor

def check(candidate):
    assert pair_xor_Sum([5,9,7,6],4) == 47
    assert pair_xor_Sum([7,3,5],3) == 12
    assert pair_xor_Sum([7,3],2) == 4

check(pair_xor_Sum)