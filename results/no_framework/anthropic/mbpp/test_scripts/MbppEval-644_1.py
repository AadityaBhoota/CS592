def reverse_Array_Upto_K(input_array, k):
    """
    Reverses the input array up to the given position 'k'.

    Args:
        input_array (list): The input array to be reversed.
        k (int): The position up to which the array should be reversed.

    Returns:
        list: The modified array with the first 'k' elements reversed.
    """
    # Reverse the first k elements of the input array
    input_array[:k] = input_array[k-1::-1]
    return input_array

def check(candidate):
    assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4) == [4, 3, 2, 1, 5, 6]
    assert reverse_Array_Upto_K([4, 5, 6, 7], 2) == [5, 4, 6, 7]
    assert reverse_Array_Upto_K([9, 8, 7, 6, 5],3) == [7, 8, 9, 6, 5]

check(reverse_Array_Upto_K)