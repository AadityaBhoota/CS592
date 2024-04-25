def reverse_Array_Upto_K(input_list, k): 
    if k > len(input_list):
        return "Error: k is greater than the length of the input list."
    
    return input_list[:k][::-1] + input_list[k:]

# Test the function with the provided examples




def check(candidate):
    assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4) == [4, 3, 2, 1, 5, 6]
    assert reverse_Array_Upto_K([4, 5, 6, 7], 2) == [5, 4, 6, 7]
    assert reverse_Array_Upto_K([9, 8, 7, 6, 5],3) == [7, 8, 9, 6, 5]

check(reverse_Array_Upto_K)