def split_Arr(l, n, k):
    """
    Splits the list 'l' at the kth element and adds the first part to the end.

    Args:
        l (list): The input list to be split.
        n (int): The length of the list 'l'.
        k (int): The index at which the list should be split.

    Returns:
        list: The modified list after splitting and adding the first part to the end.
    """
    return l[k:] + l[:k]

def check(candidate):
    assert split_Arr([12,10,5,6,52,36],2) == [5,6,52,36,12,10]
    assert split_Arr([1,2,3,4],1) == [2,3,4,1]
    assert split_Arr([0,1,2,3,4,5,6,7],3) == [3,4,5,6,7,0,1,2]

check(split_Arr)