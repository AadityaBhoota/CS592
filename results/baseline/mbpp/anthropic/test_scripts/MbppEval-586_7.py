def split_Arr(l, n, i):
    """
    Splits a list at the nth element and adds the first part to the end.

    Args:
        l (list): The input list to be split.
        n (int): The index at which the list should be split.
        i (int): The number of elements to be moved to the end.

    Returns:
        list: The modified list.
    """
    return l[i:n] + l[:i]

def check(candidate):
    assert split_Arr([12,10,5,6,52,36],2) == [5,6,52,36,12,10]
    assert split_Arr([1,2,3,4],1) == [2,3,4,1]
    assert split_Arr([0,1,2,3,4,5,6,7],3) == [3,4,5,6,7,0,1,2]

check(split_Arr)