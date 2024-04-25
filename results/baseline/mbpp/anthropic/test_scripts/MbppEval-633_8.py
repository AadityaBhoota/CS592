def pair_xor_Sum(arr, n):
    """
    Write a Python function to find the sum of XOR of all pairs of numbers in the given list.

    Examples:
    pair_xor_Sum([5,9,7,6],4) == 47
    pair_xor_Sum([7,3,5],3) == 12
    pair_xor_Sum([7,3],2) == 4
    """
    total_sum = 0
    for i in range(n):
        for j in range(i+1, n):
            total_sum += (arr[i] ^ arr[j])
    return total_sum

def check(candidate):
    assert pair_xor_Sum([5,9,7,6],4) == 47
    assert pair_xor_Sum([7,3,5],3) == 12
    assert pair_xor_Sum([7,3],2) == 4

check(pair_xor_Sum)