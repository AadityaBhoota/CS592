def reverse_Array_Upto_K(input_array, k):
    reversed_array = []
    for i in range(k):
        reversed_array.append(input_array[k-i-1])
    for i in range(k, len(input_array)):
        reversed_array.append(input_array[i])
    return reversed_array

def check(candidate):
    assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4) == [4, 3, 2, 1, 5, 6]
    assert reverse_Array_Upto_K([4, 5, 6, 7], 2) == [5, 4, 6, 7]
    assert reverse_Array_Upto_K([9, 8, 7, 6, 5],3) == [7, 8, 9, 6, 5]

check(reverse_Array_Upto_K)