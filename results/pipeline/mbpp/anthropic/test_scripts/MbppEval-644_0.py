def reverse_Array_Upto_K(input, k):
    reversed_list = []
    
    # Reverse the elements up to index k
    for i in range(k-1, -1, -1):
        reversed_list.append(input[i])
    
    # Append the remaining elements
    for i in range(k, len(input)):
        reversed_list.append(input[i])
    
    return reversed_list

def check(candidate):
    assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4) == [4, 3, 2, 1, 5, 6]
    assert reverse_Array_Upto_K([4, 5, 6, 7], 2) == [5, 4, 6, 7]
    assert reverse_Array_Upto_K([9, 8, 7, 6, 5],3) == [7, 8, 9, 6, 5]

check(reverse_Array_Upto_K)