def reverse_Array_Upto_K(input, k): 
    if not input:
        return "Input array is empty"
    
    if k >= len(input):
        return "k should be less than the length of the array"

    reversed_array = input[:k][::-1]

    result = reversed_array + input[k:]

    return result

def check(candidate):
    assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4) == [4, 3, 2, 1, 5, 6]
    assert reverse_Array_Upto_K([4, 5, 6, 7], 2) == [5, 4, 6, 7]
    assert reverse_Array_Upto_K([9, 8, 7, 6, 5],3) == [7, 8, 9, 6, 5]

check(reverse_Array_Upto_K)