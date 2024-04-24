def split_Arr(l, n, k):
    """
    Write a python function to split a list at the nth element and add the first part to the end.

    Examples:
    split_Arr([12, 10, 5, 6, 52, 36], 6, 2) == [5, 6, 52, 36, 12, 10]
    split_Arr([1, 2, 3, 4], 4, 1) == [2, 3, 4, 1]
    split_Arr([0, 1, 2, 3, 4, 5, 6, 7], 8, 3) == [3, 4, 5, 6, 7, 0, 1, 2]
    """
    if n <= 0 or n > len(l) or k <= 0 or k > n:
        return l

    first_part = l[:n-k]
    second_part = l[n-k:]
    return second_part + first_part

def check(candidate):
    assert split_Arr([12,10,5,6,52,36],2) == [5,6,52,36,12,10]
    assert split_Arr([1,2,3,4],1) == [2,3,4,1]
    assert split_Arr([0,1,2,3,4,5,6,7],3) == [3,4,5,6,7,0,1,2]

check(split_Arr)