def reverse_Array_Upto_K(input, k):
    """
    Reverses the elements of the input array up to the given position k.

    Args:
        input (list): The input array.
        k (int): The position up to which the array should be reversed.

    Returns:
        list: The modified array with the elements reversed up to position k.
    """
    # Reverse the elements up to position k
    input[:k] = input[k-1::-1]
    return input

def check(candidate):
    assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4) == [4, 3, 2, 1, 5, 6]
    assert reverse_Array_Upto_K([4, 5, 6, 7], 2) == [5, 4, 6, 7]
    assert reverse_Array_Upto_K([9, 8, 7, 6, 5],3) == [7, 8, 9, 6, 5]

check(reverse_Array_Upto_K)