def pair_xor_Sum(arr, n):
    '''
    Find the sum of xor of all pairs of numbers in the given list.

    Examples:
    pair_xor_Sum([5, 9, 7, 6], 4) == 47
    pair_xor_Sum([7, 3, 5], 3) == 12
    pair_xor_Sum([7, 3], 2) == 4
    '''

    xor_sum = 0
    
    for i in range(n):
        for j in range(i + 1, n):
            xor_sum += arr[i] ^ arr[j]
    
    return xor_sum

# Testing the function




def check(candidate):
    assert pair_xor_Sum([5,9,7,6],4) == 47
    assert pair_xor_Sum([7,3,5],3) == 12
    assert pair_xor_Sum([7,3],2) == 4

check(pair_xor_Sum)