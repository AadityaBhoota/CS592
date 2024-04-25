def reverse_Array_Upto_K(input, k):
    reversed_part = []
    for i in range(k):
        reversed_part.append(input[k-i-1])
    reversed_part.extend(input[k:])
    return reversed_part

def check(candidate):
    assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4) == [4, 3, 2, 1, 5, 6]
    assert reverse_Array_Upto_K([4, 5, 6, 7], 2) == [5, 4, 6, 7]
    assert reverse_Array_Upto_K([9, 8, 7, 6, 5],3) == [7, 8, 9, 6, 5]

check(reverse_Array_Upto_K)